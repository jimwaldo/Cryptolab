'''
Created on Oct 16, 2014

@author: waldo
'''

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


if __name__ == '__main__':
    keyfile = input('Enter name of file containing public key : ')
    f = open(keyfile, 'r')
    key = RSA.importKey(f.read())
    cipher = PKCS1_OAEP.new(key)
    
    fname = input('Enter file to encrypt : ')
    fin = open(fname, 'r')
    outname = input('Enter file name for encrypted output : ')
    fout = open(outname, 'wb')
    blocksize = 64
    while True:
        chunk = fin.read(blocksize)
        if len(chunk) == 0:
            break
        elif (len(chunk) % blocksize) != 0:
            chunk += ' ' * (blocksize - len(chunk) % blocksize)
        fout.write(cipher.encrypt(chunk))
    
    fout.close()