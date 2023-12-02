#!/usr/bin/env python

from Crypto.PublicKey import RSA

if __name__ == '__main__':
    sname = input('Enter your name : ')
    key = RSA.generate(2048)
    f = open(sname + 'key.pem', 'w')
    f.write(str(key.exportKey('PEM')))
    f.close()
    fpub = open(sname + 'pubkey.pem', 'w')
    pubkey = (key.publickey())
    fpub.write(str(pubkey.exportKey('PEM')))
    fpub.close()
