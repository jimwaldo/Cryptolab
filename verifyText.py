'''
Created on Oct 16, 2014

@author: waldo
'''
#!/usr/bin/env python

'''
Created on Oct 16, 2014

@author: waldo
'''

from Crypto.PublicKey import RSA

if __name__ == '__main__':
    keyfile = input('enter name of file containing public key : ')
    f = open(keyfile, 'rb')
    verKey = RSA.importKey(f.read())
    
    text = input('Enter text to verify : ')
    sigfile = input('Enter name of file containing verification code : ')
    fsig = open(sigfile, 'rb')
    signature = fsig.read()
    verified = verKey.verify(text, (int(signature),None))

    print(str(verified))