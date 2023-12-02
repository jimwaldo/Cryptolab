'''
Created on Oct 16, 2014

@author: waldo
'''

from Crypto.PublicKey import RSA

if __name__ == '__main__':
    keyfile = input('enter name of file containing public key : ')
    f = open(keyfile, 'r')
    verKey = RSA.importKey(f.read())
    
    fname = input('Enter file to verify : ')
    fin = open(fname, 'r')
    text = fin.read()
    sigfile = input('Enter name of file containing verification code : ')
    fsig = open(sigfile, 'r')
    signature = fsig.read()
    verified = verKey.verify(text, (int(signature),None))
    print(verified)
