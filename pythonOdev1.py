"""
Ödev-1:Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.

Ödev-2:İsimlerden oluşan üç değişkene yaş değerleri atanır.Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır.
Bu karşılaştırmalara mantıksal operatörler de eklenir.

Ödev-3:Kullanıcıdan iki değer girmesini istenir.Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.

Ödev-4:Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.

Ödev-5:"Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.
İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.
İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ")
İfadeyi hepsini büyük harf olacak hale çevrilir.("hi-kod veri bilimi atölyesi")

"0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579") """

#Ödev-1#
x = 3
y = 4.5
z = "10"

print(type(x))
print(type(y))
print(type(z))

x = float(x)
print(type(x))

x = str(x)
print(type(x))

y = int(y)
print(type(y))

y = str(y)
print(type(y))

z = int(z)
print(type(z))

z = float(z)
print(type(z))
print("**********")

#Ödev-2#
ahmet = 21
merve = 30
ayşe = 12

print(ahmet > merve) #False#
print(ahmet >= ayşe)  #True#
print(merve < ayşe)  #False#
print(ayşe <= ahmet)  #True#
print(ayşe == merve)   #False#
print(ahmet != ayşe)  #True#
print(ahmet > ayşe or merve >= ahmet)  #True#
print(ayşe > merve or ahmet <= ayşe)  #False#
print(ayşe < merve and ahmet == merve)  #False#
print(ahmet < merve and ahmet >= ayşe)  #True#
print(not(ayşe > merve))  #True#
print(not(ahmet < merve))  #False#
print("**********")

#Ödev-3#
sayi1 = int(input("Birinci sayıyı giriniz: "));
sayi2 = int(input("İkinci sayıyı giriniz: "));

toplama = sayi1+sayi2
cikarma = sayi1-sayi2
carpim = sayi1*sayi2
bolme = sayi1/sayi2

print("Toplama: ",toplama , "Çıkarma: ",cikarma ,"Çarpma: ",carpim, "Bölme: ",bolme)
print("**********")

#Ödev-4#
isim = input("İsminizi giriniz: ");
yas = int(input("Yaşınızı giriniz: "));
sehir = input("Yaşadığınız şehri yazınız: ");
meslek = input("Mesleğinizi yazınız: ");

print("İsmi: ",isim,"Yaşı: ",yas ,"Şehir: ",sehir,"Meslek: ",meslek)
print("**********")

#Ödev-5#
atolye = "Hi-Kod Veri Bilimi Atölyesi"

print(atolye[0:6])
print(atolye[7:11])
print(atolye[12:18])
print(atolye[19:])

print(atolye.upper())
print(atolye.lower())

sayilar = "0123456789"
print(sayilar[0:9:2])
print(sayilar[1::2])

#FATMA ÖZDEMİR#