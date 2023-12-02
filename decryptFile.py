'''
Created on Oct 16, 2014

@author: waldo
'''

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

if __name__ == '__main__':
    keyfile = input('Enter name of file containing private key : ')
    f = open(keyfile, 'rb')
    key = RSA.importKey(f.read())
    cipher = PKCS1_OAEP.new(key)
    blocksize = 64
    
    fname = input('Enter file to decrypt : ')
    fin = open(fname, 'rb')
    outname = input('Enter file name for decrypted output : ')
    fout = open(outname, 'w')
    
    while True:
        chunk = fin.read(blocksize)
        if len(chunk) == 0:
            break
        fout.write(str(cipher.decrypt(chunk)))
    
    fout.close()