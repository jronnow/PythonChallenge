#!/usr/bin/env python
import string, re
f = open(r'encryptedMess.txt', 'r') # The r before the filepath converts the following string to a raw string so Python doesn't interpret the backslashes as escape characters, and the 'r' after it specifies that we're opening it for reading
mess = f.read()
# We now have the plaintext as a string variable stored in mess, so we can close the .txt file
f.close()
r = re.compile('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+')
print(''.join(r.findall(mess)))