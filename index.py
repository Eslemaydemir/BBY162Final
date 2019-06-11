# author= Eslem Aydemir
class islem:
    print("Kütüphaneye hoşgeldin")
    print("Kütüphanede bulunan kitaplar;")
def katlistele(self):
    listele= open("kitap.txt", "r+", encoding="utf-8")
d = {}
with open("kitap.txt") as f:
    for line in f:
        (key, val) = line.split(",")
        d[str(key)] = val
    print (d)

def kayitekle(self):
        ekle = open("kitap.txt", "a",)
        with open("kitap.txt", "a") as f:
          f.write("n\Yasar Kemal, Ince Mehmed")

def eserarama(self):
    ekayitara = open("kitap.txt", "r", encoding="utf-8")
d = {}
with open("kitap.txt") as f:
    for line in f:
        (key, val) = line.split(",")
        d[str(key)] = val
        a = str(val)
    i = input("Yazarın Eserini Arayın:")
    if i in d:
        eyazdir= "{} yazdığı kitaplar: {}"
        print(eyazdir.format(i,d[i]))
    else:
        print("Aradığınız kitap kütüphanemizde bulunmamaktadır.")

def yazararama(self):
    ykayitara = open("kitap.txt", "r", encoding="utf-8")
dic = {}
with open("eser.txt") as f:
    for line in f:
        (key, val) = line.split(",")
        dic[str(key)] = val
        a = str(val)
    i = input("Kitabın yazarını arayın:")
    if i in dic:
        yyazdir= "{} kitabının yazarı: {}"
        print(yyazdir.format(i,dic[i]))
    else:
        print("Aradığınız kitap kütüphanemizde bulunmamaktadır.")

katalog = islem()
