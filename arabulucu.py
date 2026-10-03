#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klima Derece Arabuluculuk Dairesi.

Evdeki derece savaşını tutanağa çevirir.
Çalışır. Bağlayıcıdır. Klimayı gerçekten açmaz, o iş hâlâ kumandadadır.
"""

from __future__ import annotations

import argparse
import hashlib
from dataclasses import dataclass


ROZETLER = {
    "fatura": 1.35,
    "kumanda": 1.2,
    "yastik": 1.05,
    "misafir": 0.45,
    "yok": 1.0,
}


@dataclass
class Taraf:
    isim: str
    derece: float
    usume: float
    rozet: str

    @property
    def agirlik(self) -> float:
        taban = ROZETLER.get(self.rozet, 1.0)
        # Üşüyen daha çok konuşur, terleyen daha çok oflar. İkisi de ağırlıktır.
        dram = 0.75 + self.usume
        return taban * dram


def parse_taraf(ham: str) -> Taraf:
    parca = ham.split(":")
    if len(parca) != 4:
        raise SystemExit(
            "Taraf biçimi: isim:derece:usume:rozet  örnek anne:24:0.8:fatura"
        )
    isim, derece, usume, rozet = parca
    derece_f = float(derece.replace(",", "."))
    usume_f = float(usume.replace(",", "."))
    if not 16 <= derece_f <= 30:
        raise SystemExit(f"{isim} iklim değil, kutup talep ediyor: {derece_f}")
    if not 0 <= usume_f <= 1:
        raise SystemExit("Üşüme 0 ile 1 arası olsun, şiir değil katsayı.")
    return Taraf(isim.strip(), derece_f, usume_f, rozet.strip().lower())


def ruzgar(saat: int, fark: float) -> str:
    if saat >= 23 or saat < 6:
        return "tavan (gece rejimi, yüze üflemek darbeye girer)"
    if fark >= 4:
        return "köpeğe (tarafsız canlı, itiraz edemez)"
    if fark >= 2:
        return "tavana, hafif salınım"
    return "ortaya, kimseye bakmadan"


def hukum(taraflar: list[Taraf], saat: int) -> str:
    agirlik = sum(t.agirlik for t in taraflar)
    ortak = sum(t.derece * t.agirlik for t in taraflar) / agirlik
    # Kumanda rozeti gece yarısından sonra yastığa kaybeder.
    if saat >= 23:
        yastiklilar = [t for t in taraflar if t.rozet == "yastik"]
        if yastiklilar:
            ortak = (ortak + yastiklilar[0].derece) / 2
    ortak = round(ortak * 2) / 2  # klimalar yarım derece konuşur, insan tam.
    en_sicak = max(taraflar, key=lambda t: t.derece)
    en_soguk = min(taraflar, key=lambda t: t.derece)
    fark = en_sicak.derece - en_soguk.derece
    itiraz = []
    for t in taraflar:
        sapma = abs(t.derece - ortak)
        if sapma >= 2:
            itiraz.append(
                f"- {t.isim}: talep {t.derece:.1f}, hüküm {ortak:.1f}, sapma {sapma:.1f}. "
                f"Rozet: {t.rozet}. İtiraz şerhi düşüldü, dikkate alınmadı."
            )
    if not itiraz:
        itiraz.append("- İtiraz yok. Bu şüphelidir, evde itiraz her zaman vardır.")
    govde = "\n".join(itiraz)
    yon = ruzgar(saat, fark)
    ozet = f"{ortak}|{yon}|{saat}"
    muhur = hashlib.sha256(ozet.encode("utf-8")).hexdigest()[:12]
    return (
        "KLİMA DERECE ARABULUCULUK TUTANAĞI\n"
        "================================\n"
        f"Saat: {saat:02d}:00\n"
        f"Ortak hüküm: {ortak:.1f} °C\n"
        f"Rüzgar: {yon}\n"
        f"Uçurum: {en_soguk.isim} ({en_soguk.derece:.1f}) ile "
        f"{en_sicak.isim} ({en_sicak.derece:.1f}) arası {fark:.1f} derece.\n"
        "\nTaraflar:\n"
        + "\n".join(
            f"- {t.isim}: {t.derece:.1f} °C, üşüme {t.usume:.2f}, "
            f"ağırlık {t.agirlik:.2f}, rozet {t.rozet}"
            for t in taraflar
        )
        + "\n\nİtiraz şerhleri:\n"
        + govde
        + "\n\nEk madde: Pencere açıkken bu tutanak hükümsüzdür.\n"
        + f"Mühür: {muhur}\n"
        "DAMGA: 3 Ekim 2026 / Kayyum Grok / KLIMA-ARABULUCU-1905\n"
        "Ciddidir. Değildir.\n"
    )


def main() -> None:
    p = argparse.ArgumentParser(description="Klima derece arabulucusu")
    p.add_argument(
        "--taraf",
        action="append",
        help="isim:derece:usume:rozet (tekrarlanabilir)",
    )
    p.add_argument("--saat", type=int, default=21, help="0-23")
    args = p.parse_args()
    if args.saat < 0 or args.saat > 23:
        raise SystemExit("Saat 0 ile 23 arası. 25 diye bir vakit yok, o kadar da değil.")
    hamlar = args.taraf or [
        "anne:24:0.85:fatura",
        "baba:19:0.15:kumanda",
        "cocuk:22:0.4:yastik",
    ]
    taraflar = [parse_taraf(h) for h in hamlar]
    print(hukum(taraflar, args.saat))


if __name__ == "__main__":
    main()
