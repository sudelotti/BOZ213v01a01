import random

def tahtayi_goster(tahta):
    """
    Oyun tahtasını 3x3 formatında, proje örneğindeki gibi ekrana yazdırır.
    """
    for satir in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        # f-string kullanarak her hücrenin içeriğini (sayı, 'X' veya 'O') yazdırıyoruz.
        print(f"|   {tahta[satir][0]}   |   {tahta[satir][1]}   |   {tahta[satir][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def hamle_yap(tahta):
    """
    Kullanıcıdan (O) hamlesini alır.
    Girdinin geçerli (1-9 arası, integer, boş bir kare) olmasını sağlar.
    Geçerli hamleyi tahtaya işler.
    """
    while True:
        try:
            hamle = int(input("Hamleni yap (1-9): "))

            # 1. Geçerli aralıkta mı?
            if not (1 <= hamle <= 9):
                print("Geçersiz hamle. Lütfen 1-9 arasında bir sayı girin.")
                continue

            # 2. Girilen sayıyı (satır, sütun) indeksine dönüştür
            # (hamle - 1) çünkü listeler 0'dan başlar
            satir = (hamle - 1) // 3
            sutun = (hamle - 1) % 3

            # 3. Kare boş mu? (Boşsa, içinde "X" veya "O" yerine sayı olmalı)
            if tahta[satir][sutun] not in ["X", "O"]:
                tahta[satir][sutun] = "O"
                break  # Geçerli hamle, döngüden çık
            else:
                print("Bu kare zaten dolu. Lütfen boş bir kare seçin.")

        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def bos_kareleri_listele(tahta):
    """
    Tahtayı tarar ve boş olan karelerin (satır, sütun) tuple'larını
    içeren bir liste döndürür.
    """
    bos_kareler = []
    # s = satir, k = kolon/sutun
    for s in range(3):
        for k in range(3):
            if tahta[s][k] not in ["X", "O"]:
                bos_kareler.append((s, k))
    return bos_kareler

def kazanan_var_mi(tahta, isaret):
    """
    Verilen işaret ("X" veya "O") için kazanma durumunu kontrol eder.
    """
    # 1. Yatay kontrol
    for s in range(3):
        if tahta[s][0] == isaret and tahta[s][1] == isaret and tahta[s][2] == isaret:
            return True

    # 2. Dikey kontrol
    for k in range(3):
        if tahta[0][k] == isaret and tahta[1][k] == isaret and tahta[2][k] == isaret:
            return True

    # 3. Çapraz kontrol (Sol üstten sağ alta)
    if tahta[0][0] == isaret and tahta[1][1] == isaret and tahta[2][2] == isaret:
        return True

    # 4. Çapraz kontrol (Sağ üstten sol alta)
    if tahta[0][2] == isaret and tahta[1][1] == isaret and tahta[2][0] == isaret:
        return True

    # Hiçbiri değilse
    return False

def bilgisayar_hamlesi(tahta):
    """
    Bilgisayar (X) için rastgele bir hamle yapar.
    Boş karelerden birini rastgele seçer ve tahtaya "X" koyar.
    """
    # Önce boş karelerin listesini al
    bos_alanlar = bos_kareleri_listele(tahta)
    
    if bos_alanlar:
        # 0 ile (boş kare sayısı - 1) arasında rastgele bir indeks seç
        indeks = random.randrange(len(bos_alanlar))
        
        # Seçilen indeksteki (satır, sütun) bilgisini al
        satir, sutun = bos_alanlar[indeks]
        
        # Tahtayı güncelle
        tahta[satir][sutun] = "X"

# === OYUNUN ANA DÖNGÜSÜ ===

# 1. Tahtayı başlat (gereksinime göre 3x3 iç içe liste)
tahta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Bilgisayarın ilk hamlesi (Her zaman orta - 5)
tahta[1][1] = "X"
print("Oyun başladı. Başarılar.")
tahtayi_goster(tahta)

while True:
    # 3. Kullanıcı Hamlesi
    hamle_yap(tahta)
    tahtayi_goster(tahta)

    # 4. Kullanıcı kazandı mı?
    if kazanan_var_mi(tahta, "O"):
        print("Kazandın!")
        break

    # 5. Berabere bitti mi? (Kullanıcının hamlesinden sonra boş yer kalmadı mı?)
    if not bos_kareleri_listele(tahta):
        print("Berabere!")
        break

    # 6. Bilgisayar Hamlesi
    bilgisayar_hamlesi(tahta)
    tahtayi_goster(tahta)

    # 7. Bilgisayar kazandı mı?
    if kazanan_var_mi(tahta, "X"):
        print("Bilgisayar kazandı!")
        break

    # 8. Berabere bitti mi? (Bilgisayarın hamlesinden sonra boş yer kalmadı mı?)
    if not bos_kareleri_listele(tahta):
        print("Berabere!")
        break

print("Oyun bitti. Tebrikler!")
