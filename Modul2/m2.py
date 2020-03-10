class Pesan(object):
    def __init__(self, a):
        self.text = a
    def cI(self):
        print(self.text)
    def cPHB(self):
        print(str.upper(self.text))
    def cPHK(self):
        print(str.lower(self.text))
    def jumK(self):
        return len(self.text)
    def cJKar(self):
        print('Kalimatku mempunyai', len(self.text),'Karakter')
    def perbarui(self,sB):
        self.text=sB
        
class sK(object):
    def mS(self):
        pass
    def mSm(self,sb):
        pass
