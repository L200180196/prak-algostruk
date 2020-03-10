from m3 import Manusia 
class SiswaSMA(Manusia):
    listmapel=[]
    def __init__(self):
        self.nama = str(input("Masukkan Nama : "))
        self.nis = str(input("Masukkan NIS : ")) 
        self.kotaTinggal= str(input("Masukkan Kota Tinggal : "))
        self.kls= str(input("Masukkan Kelas : "))
    def __str__(self):
        a = self.nama +', NIM '+str(self.NIM)\
            +'. Tinggal di '+self.kotaTinggal\
            +'. Berada di Kelas '+str(self.kls)
        return a
    def ambilmapel(self,a):
        self.listmapel.append(a)
    def hapusmapel(self,a):
        self.listmapel.remove(a)
