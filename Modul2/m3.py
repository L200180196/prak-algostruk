class Manusia(object):
    keadaan='lapar'
    def __init__(self,nama):
        self.nama = nama
    def uS(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan='kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan",k)
        self.keadaan='lapar'
    def mDD(self,n):
        return n*2
