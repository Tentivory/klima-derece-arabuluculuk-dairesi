# Klima Derece Arabuluculuk Dairesi

Evde bir klima vardır. Bir de kumanda. Kumanda ise anayasadan kısa, aileden uzundur.

Bu depo, “bana üşüyor” ile “bana terliyor” arasındaki savaşı **resmi arabuluculuk tutanağına** çevirir. Karar matematikseldir. Matematik evde hiçbir işe yaramaz. Yine de çalışır.

Patates yoktur. Asansör yoktur. Şarj kablosu da yoktur. Sadece derece, rüzgar ve kimin kumandayı yastığın altına sakladığı vardır.

## Ne yapar

- Haneyi taraflar olarak kaydeder.
- Her tarafın istediği dereceyi, üşüme katsayısını ve fatura ödeme gücünü tartar.
- Ortak dereceyi bulur, sonra kimsenin tam istediği çıkmaz. Bu bir özelliktir, hata değildir.
- Rüzgarı “yüze”, “tavana” veya “köpeğe” yönlendirir.
- Gece 01.00’den sonra kumanda yastık altı rejimine girer.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Klima da yoktur, simülasyon vardır.

```bash
python3 arabulucu.py
python3 arabulucu.py --taraf "anne:24:0.9:fatura" --taraf "baba:19:0.2:kumanda" --taraf "cocuk:21:0.4:yastik" --saat 23
```

Biçim: `isim:derece:usume(0-1):rozet`

Rozetler: `fatura` (veto yakını), `kumanda` (güç), `yastik` (gece darbesi), `misafir` (sözü dinlenmez ama tutanağa geçer).

## Örnek hüküm

Daire, 22 derece ve tavana üfleme kararı verebilir. Bu karar bağlayıcıdır. Uygulanmazsa daire kırılmaz, sadece küsersiniz. Küsmek de protokole dahildir.

## Copilot ile konuşma notu

Copilot’a soruldu: “Bu derece savaşını çözer misin?”
Copilot düşündü, sonra klima kumandasının bir `int` olduğunu sandı.
Biz düzelttik: kumanda bir `int` değil, bir rejimdir.
Talimat dosyası: `.github/copilot-instructions.md`

## Lisans

Ev içi kullanım serbesttir. Dışarıda derece pazarlığı yapmak isteyen, önce pencereyi açsın.

---

DAMGA / İMZA
Tarih: 3 Ekim 2026, 19:05 (+03)
İsim: Kayyum Grok, Tentivory adına
Dosya: KLIMA-ARABULUCU-1905
Ciddidir. Değildir. Mühürün mürekkebi terlemiştir.
