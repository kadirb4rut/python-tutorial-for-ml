# %% Değişkenler

a = 5
b = 12.4
sentece = "selam kadir"
print(type(a),type(b),type(sentece))

print("Toplam : ", a+b)

# %%   Print Özellikleri

a = 100
b = 25.8
ondalikliSayi = 15.2897697

print("A Sayısı : {} B Sayısı : {}".format(a,b))
print("Ondalıklı Sayı : %.2f B Sayısı = %.1f" % (ondalikliSayi,b))

# %% Değişkenler arası dönüşüm

a = 15
b = 30.5

c = int(b)

print(c)

d = float(a)

print(d)

# %% If-Else, Döngü vs Girintileri

if 5<10:
    print("Sayı 10'dan küçüktür")
else:
    print("Sayı 10'dan büyüktür")
    
# %% Listeler
    
"""
- Birleşik veri türüdür. Çok yönlüdür.
- Farklı tür değişkenleri bir arada tutabilirler.
- [1,"kadir",5.2] gibi

"""
liste = [1,2,3,4,5,6]
print(type(liste))

hafta = ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
print(hafta[0])

print(len(hafta)) # listenin boyutunu verir.

print(hafta[-1]) # Listenin son elemanını verir.

print(hafta[1:3]) # 1'den 3'e kadar, 1 dahil, 3 dahil değildir !!!

liste.append(7) # Listeye ekleme komutu append() metodu
print(liste)

liste.remove(4) # Listeden eleman siler.
print(liste)

liste.reverse() # Listeyi ters çevirir.
print(liste)

liste.sort() # elemanları sıralar
print(liste)

# %% Tuple Veri Tipi

"""
- Değiştirilemez ve sıralı bir veritipidir.
- (3,4,5) gibi tanımlanır.

"""

tuple_veritipi = (1,2,3,3,4,5,6)

print(tuple_veritipi[0])

print(tuple_veritipi[2:]) # 2. index dahil ve 2'den sonra hepsini yazdırır.

print(tuple_veritipi.count(3)) # İçinde kaç tane 3 olduğunu bulur.

tuple_xyz = 1,2,3
x, y, z = tuple_xyz # x,y,z yi ayrıştırır ve sırasıyla değerleri x,y,z ye atar.

print("X sayısı : {} Y sayısı {} Z sayısı {}".format(x,y,z))

# %% IF - ELSE Kullanımı

liste = [1,2,3,4,5,6]
deger =32

if deger in liste:
    print("{} değeri listede var.".
          mat(deger))
else:
    print("{} degeri listede yok.".format(deger))
    

sozluk = {"Türkiye" : "Ankara", "İngiltere" : "Londra", "İspanya" : "Madrid"}
ulke = "Türkiye"

dictkeys = sozluk.keys()

if ulke in dictkeys:
    print("Belirttiğiniz ülke sözlük listesi içerisinde var.")
else:
    print("Belirttiğiniz ülke sözlük listesi içerisinde yok.")
    
sayi1 = 50
sayi2 = 100

if sayi1>40 or sayi2>40:
    print("sayı 40'tan büyüktür.")
else:
    print("sayılar 40'tan küçüktür.")
    
if sayi1<40 and sayi2<40:      # Her iki sayının da büyük olma durumu
    print("sayılar 40'tan küçüktür.")
else:
    print("sayılar 40'tan büyüktür.")
    
# %% DONGULER
    
"""
 - Bir dizi üzerinde yineleme yapmak için kullanılan yapılardır.
 - Diziler : Liste, Tuple, String, Dictionary, Numpy ve Pandas veri tipleri

"""

# For Döngüsü

for i in range(1,11): # İterasyon yani i değişkeni sırasıyla 1,2,3,4.... olacak.
    print(i)

# For Dögüsü ile Listedeki elemanları toplama     
liste = [1,4,5,6,8,3,3,4,67]
toplam=0
for i in liste:
    toplam += i
    
print(toplam)

# Sum Fonksiyonu ile Listedeki elemanları toplama

print(sum(liste))

# Tuple dizisi ile For döngüsü kullanımı

tup1 = ((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x,y,z)
    
# %% Fonksiyonlar
    
"""
 - Karmaşık işlemleri bir araya toplar ve tek adımda yapmamızı sağlar.
 - Şablon oluştururlar.
 - Düzenleme
 
"""

# Kullanıcı tarafından tanımlanan fonksiyonlar

def toplam(sayi1,sayi2):
    sonuc = sayi1 + sayi2
    print("{} sayısı ile {} sayısının toplamı : {}".format(sayi1,sayi2,sonuc))
    

toplam(5,12)

# Return ile Fonksiyon kullanımı

def carpma(sayi3,sayi4):
    return sayi3*sayi4

carpmaSonuc = carpma(4,8)
print("Çarpma İşleminin sonucu = ",carpmaSonuc)

# NOT: Classların içinde kullanılıyorsa METHOD, Classların dışında kullanılır ise FONKSİYON denir.

# Fonksiyon içerisinde Default değer tanımlama

def daireAlan(r, pi = 3.14): # Pi default olarak tanımlanmıştır.
    return pi*(r**2)

alanSonuc = daireAlan(10)
print("Dairenin alanı = ",alanSonuc)


# Boş Fonksiyon Tanımlama

"""
Bazı Derin Öğrenme kütüphaneleri parametre olarak fonsiyon istiyor,
 bu durumda Boş Fonksiyon oluşturabiliriz.

"""

def bos():
    pass    

# Lambda Fonksiyon Tanımlama
    
"""
 - Lambda fonksiyonlar ileri seviyeli fonksiyonlardır.
 - Küçük ve anonim işlemdir.
 - 
 
"""

def carpma(x,y,z):
    return x*y*z

sonuc = carpma(2,3,4)
print(sonuc)

# Aynı işlemi Lambda fonksiyonu ile yapalım.

lambdaSonuc = lambda x,y,z : x*y*z
print(lambdaSonuc(2, 3, 4))

# %% Numpy Kütüphanesi

"""
 - Matrisler için hesaplama kolaylığı sağlar.
 
"""

# 1*15 boyutunda vektör bir numpy array 

import numpy as np

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) # --> boyutu

dizi2 = dizi.reshape(3,5) # Yeniden boyutlandırma, 2 boyutlu matris yapmak.
print(dizi2)

print("Şekil : ",dizi2.shape)

print("Boyut : ",dizi2.ndim) # Kaç boyutlu olduğunu öğrenme

print("Veri Tipi :",dizi2.dtype)

print("Boyu : ", dizi2.size)

print("Type : ",type(dizi2))

# 2 boyutlu array

dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)

# Sıfırlardan oluşan bir Array oluşturma

npZeros = np.zeros((3,4)) # 2 TANE PARANTEZ!!! UNUTMA!!!
print(npZeros)

# Birlerden oluşan bir Array oluşturma

npOnes = np.ones((3,4)) # 2 TANE PARANTEZ!!! UNUTMA!!!
print(npOnes)

# Boş Array

npEmpty = np.empty((3,4)) # 2 TANE PARANTEZ!!! UNUTMA!!!
print(npEmpty)

# Arange kullanımı (x,y,basamak)

dizi_aralik = np.arange(10,50,5) # --> 10'dan başlasın 50'ye kadar 5'er artsın.
print(dizi_aralik)

# Linspace kullanımı (x,y,basamak)

dizi_bosluk = np.linspace(10,20,5) # 10 ve 20 arasını 5'e böler. 10 ve 20 dahil!!!
print(dizi_bosluk)

# Float Array Kullanımı

float_array = np.float32([[1,2],[3,4]])
print(float_array)

# %% Matematiksel İşlemler

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Toplama : ",a+b)
print("Çıkarma : ",a-b)
print("{} Karesi : {}".format(a,a**2))
print("{} Karesi : {}".format(b,b**2))


# Numpy Dizi Elemanlarını toplamak

print(np.sum(a))  

# Numpy Dizi içindeki MAX değer bulma

print(np.max(a))

# Numpy Dizi içindeki MIN değer bulma

print(np.min(a))

# Mean Ortalama

print(np.mean(a))

# Median(Ortadaki Sayı)

print(np.median(a))

# Random Sayı oluşturma [0,1] arasında sürekli uniform 3*3

rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

# Numpy Index işlemleri

dizi = np.array([1,2,3,4,5])
print(dizi[0])

# Dizinin ilk 4 elemanını almak için

print(dizi[0:4])

# Dizinin Tersini Almak

print(dizi[::-1])

# 2 Boyutlu dizi oluşturmak

dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

# Dizinin 1. satır ve 1. sütununda bulunan elemanı yazdıralım.

print(dizi2D[1,1])

# Dizinin 1. Sütununun tüm satırlarını alalım.

print(dizi2D[:,1])

# Dizinin birinci satırının 1,2,3. sütunlarını alalım.

print(dizi2D[1,1:4])

# Dizinin son satırının tüm sütunları

print(dizi2D[-1,:])

# 2 boyutlu diziyi(Matris) tek boyutlu diziye(Vektör) çevirme. Ravel Özelliği

dizi2D = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print(dizi2D)

diziVector = dizi2D.ravel() # Matrisi Vektöre yani tek boyuta çevirir!!!
print(diziVector)

# Maximum sayının indexini bulmak

maxIndex = diziVector.argmax()
print(maxIndex)

# %% Pandas Kütüphanesi

"""
 - Hızlı, güçlü ve esnek veri analizi
 - DataFrame oluşturma, Çerçeve

"""
import pandas as pd

# Sözlük Oluştur

dictionary = {"isim" : ["Ali","Veli","Kenan","Murat","Ayşe","Hilal"],
              "yas" : [15,16,17,33,45,66],
              "maas" : [100,150,240,350,110,220]}

# Dictionary'i DataFrame'e Çevir!!!!!!!

veriDF = pd.DataFrame(dictionary)
print(veriDF)

# DataFrame veya verinin ilk 5 satırına hızlıca göz atmak için

print(veriDF.head())

# Veri Sütunlarını yazdır

print(veriDF.columns)

# Veri Hakkında bilgi Elde etmek

print(veriDF.info()) # Veri ile ilgili temel bilgiler, Veri hakkında ilk izlenim

# İstatistiksel Özellikler

print(veriDF.describe())

# Yas Sütunu

print(veriDF["yas"])

# Sütun Eklemek

veriDF["sehir"] = ["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]
print(veriDF)

# Yaş Sütunu

print(veriDF.loc[:,"yas"])

# Yas Sütunu ve ilk 3 satır

print(veriDF.loc[:2,"yas"])

# Yas ve Şehir arası Sütunları ve ilk 3 satır

print(veriDF.loc[:2,"yas" : "sehir"]) # yas ve sehir dahil!!!!

print(veriDF.loc[:2,["isim","yas"]])

# Satırları tersten yazdır.

print(veriDF.loc[::-1,:])

# yas sütunu with "iloc" --> "iloc" Kullanımı

print(veriDF.iloc[:,1])

print(veriDF.iloc[:,:3])

# Yas ve Şehir arası Sütunları ve ilk 3 satır with "iloc" !!!!!!!!

print(veriDF.iloc[:2,[0 , 1]])

# %% DataFrame Filtreleme
import pandas as pd

dictionary = {"isim" : ["Ali","Veli","Kenan","Murat","Ayşe","Hilal"],
              "yas" : [15,16,17,33,45,66],
              "sehir" : ["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"]}

veriDf = pd.DataFrame(dictionary)
print(veriDf)

# İlk olarak yaşa göre bir filtre oluşturuyoruz. yas > 22

filtre1 = veriDf.yas > 22  # VeriDf'deki yas sütununu ve oradaki 22 den büyük olan verileri getir.

filtrelenmisVeri = veriDf[filtre1]
print(filtrelenmisVeri)

# Ortalama Yaş

"""
 * BURASI ÖNEMLİ * DataFrame Üzerinde IF - ELSE ve For döngüsü sorgusu çalıştırmak.
 
"""
ortalamaYas = veriDf.yas.mean() # Yaş sütununa göre Ortalama yaş bulunur.

veriDf["YAS_GRUBU"] = ["kucuk" if ortalamaYas > i else "buyuk" for i in veriDf.yas]
print(veriDf)

# Birleştirme

sozluk1 = {"isim" : ["Ali","Veli","Kenan"],
           "yas"  : [15,16,17],
           "sehir" : ["İzmir","Ankara","Konya"] }

veri1 = pd.DataFrame(sozluk1)

# 2. Verisetini Oluşturalım.

sozluk2 = {"isim" : ["Murat","Ayşe","Hilal"],
           "yas"  : [33,45,66],
           "sehir" : ["Ankara","Ankara","Antalya"] }

veri2 = pd.DataFrame(sozluk2)

# Dikey olarak birleştirme

veri_dikey = pd.concat([veri1,veri2], axis = 0)

print(veri_dikey)

# Yatay olarak birleştirme

veri_yatay = pd.concat([veri1,veri2], axis = 1)

print(veri_yatay)

"""
 * NOT : Farklı Sütunlara sahipsek yatayda birleştirme yapmalıyız.
         Fakat aynı sütunlara sahipsek dikeyde birleştirmek daha mantıklıdır!!!
         
"""

# %% Matplotlib Veri Görselleştirme Kütüphanesi

"""
 - Veri Görselleştirme Kütüphanesi
 
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure()
plt.plot(x,y,color = "red", alpha = 0.5, label = "line") # alpha değeri saydamlık verir. 0 ile 1 arası değer alır.
plt.scatter(x,y, color = "blue",alpha = 0.5, label = "scatter") # parçacık eklemek için kullanılır.
plt.legend() # label değerinin grafikte görünmesi için legend() metodu kullanılır.
plt.title("Matplotlib")
plt.xlabel("X") # xlabel ile X eksenini isimlendirebiliriz.
plt.ylabel("Y") # ylabel ile Y ekseni isimlendirme.
plt.grid(True) # Grid ekleme. Yani köşegen çizgiler eklemek
plt.xticks([0,1,2,3,4,5])
plt.show() # Plotu kapatma olarak düşün. Disconnect




# %% OS Kütüphanesi

"""
 - Bilgisayardaki klasör,saat,tarih vb. yerel işlemleri yapmamızı sağlar

"""

import os

print(os.name) # Bilgisayarın İşletim Sistemi nedir?

currentDir = os.getcwd() # Hangi klasörde bulunuyoruz ?

print(currentDir)

# Create New Folder

folderName = "new_folder"
os.mkdir(folderName)

# Change Folder Name

newFolderName = "Changed Folder Name"
os.rename(folderName,newFolderName)

# Change Directory

os.chdir(currentDir+"/"+newFolderName)
print(os.getcwd())

# Bulunduğumuz klasördeki dosyaları öğrenmek

files = os.listdir() # Liste olarak döndürür.
print(files)

# For döngüsü ile bu klasördeki dosyalardan ".py" uzantılı olanları görüntülemek

for i in files:
    if i.endswith(".py"):
        print(i)

# Klasör silmek
        
os.rmdir(newFolderName)

""" 
    Şimdi bir klasörün altındaki dizinleri ve dosyaları görebileceğimiz 
    bir method yazalım.
    
"""

for i in os.walk(currentDir): # "walk" dosya içinde dolaş anlamında sonra print ile yazdır.
    print(i)
    
    
# Exist ile aradığımız dosya var mı, yok mu ? kontrolü.
    
os.path.exists("PythonBasics.py") # Dosya varsa "True" değeri döndürür.

# %%

 







