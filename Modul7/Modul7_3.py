#Nomer 3

import re
f=open('IndonesiaWiki.txt','r', encoding='latin1')
baca = f.read()
f.close()
kata = r'di \w+'
diTempat= re.findall(kata,baca)
print(diTempat)
