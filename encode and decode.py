##Base64
##MD5
##DES
##3DES
##AES
## RSA


import hashlib

s = 'hello Julian'

h1 = hashlib.md5() #付函数 好
h1.update(s.encode(encoding='utf8')) #加密
print(h1.hexdigest()) #打印加密后的字符串

