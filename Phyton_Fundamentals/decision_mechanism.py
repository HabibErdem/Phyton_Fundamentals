# Örnekler:

#-1 ) Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini gösteren python kodu (50den büyükse geçti değilse kaldı)

# Ders_ortalamasi=int(input('Ders notunuzu giriniz: '))
# if Ders_ortalamasi >= 50:
#     print('Terbrikler geçtiniz. ')
# else:
#     print('Üzgünüm, kaldınız')

#-2 ) Klavyeden girilen sayının tek mi çift mi olduğunu yazdıran python kod

# sayi=int(input(' Bir sayı giriniz: '))
# if sayi %2 == 0 :
#     print(' Girilen sayı Çifttir ')
# else:
#     print(' Girilen satı tektir. ')

#-3) Klavyeden girilen sayının pozitif mi negatif mi yoksa sıfır mı olduğunu gösteren kod.

# sayi=int(input('Bir sayı giriniz: '))
# if sayi > 0 :
#     print('Girilen sayı pozitif bir sayıdır ')
# elif sayi == 0:
#     print('Girilen sayı nötr bir sayıdır ')
# else:
#     print('Girilen sayı negatif bir sayıdır. ')

#-4)  Kullanıcının yaşına göre ehliyet alıp alamayacağını bildiren kod.


# yas=int(input('Yaşınızı giriniz: '))
#
# if yas>=18:
#     print('Ehliyet alabilirsinsiniz')
# else:
#     print('Yaşınız tutmuyor, ehliyet alamazsınız ')

#-5) Bir internet satış sitesi alışveriş tutarı 1000 TL’nin üzerindeki siparişlerde kargo bedava. 1000 TL altı
#sipariş tutarına ise 50 TL ek kargo ücreti ilave ediyor ve ekrana kargo ücreti ile birlikte toplam tutarı yazıyor.
#bu programın kodu.

# tutar=int(input('Alışveriş tutarını giriniz: '))
# if tutar < 1000:
#     print('Kargo ücreti ile birlikte toplam tutar :',tutar+50 )
# else:
#     print('Kargo ücreti yoktur. Toplam tutar: ', tutar )

#6-) Kullanıcıya boyunun kaç cm olduğunu soran ve eğer boyu 1.70 cm’den kısa ise “Boyunuz kısa”,
#boyu 1.70 ile 1.80 cm arasında ise “Boyunuz orta”, 1.80 cm’den fazla ise “Boyunuz uzun” yazan programın kodu.

# boy=float(input(' Boyunuzu giriniz:  '))
#
# if boy <= 1.70:
#     print('Boyunuz kısa ')
# elif boy <= 1.80:
#     print(' Boyunuz orta')
# elif boy > 1.80:
#     print('Boyunuz uzun')

#7-) Bir otopark ücret tarifesi şöyledir:
# 0 – 3 saat arası : 3 TL,
# 3 – 7 saat arası : 4 TL,
# 7 – 12 saat arası : 5 TL,
# 12 saat ve üzeri 6 TL
# Buna göre girilen saate göre otoparka ödenecek ücreti hesaplayıp ekrana yazdıran,kod.

# sure=int(input('Süre? : '))
#
# if sure <= 3:
#     print('Otopark ücreti: ', sure*3)
# elif sure > 3 and sure <= 7:
#     print(' Otopark ücteri: ',sure*4)
# elif sure > 7 and sure <= 12:
#     print(' Otopark ücteri: ', sure *5)
# else:
#     print('Otopark süresi: ', sure*6)


