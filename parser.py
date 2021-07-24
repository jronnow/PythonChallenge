#!/usr/bin/env python
import string, re
f = open(r'encryptedMess.txt', 'r') 
mess = f.read()
# We now have the plaintext as a string variable stored in mess, so we can close the .txt file
f.close()
r = re.compile('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+')
print(''.join(r.findall(mess)))
