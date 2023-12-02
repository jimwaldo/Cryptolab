#!/usr/bin/env python
'''
Created on Oct 16, 2014

@author: waldo
'''

from Crypto.PublicKey import RSA

if __name__ == '__main__':
    keyfile = input('enter name of file containing private key : ')
    f = open(keyfile, 'r')
    signKey = RSA.importKey(f.read())
    
    text = input('Enter text to sign : ')
    signature = signKey.sign(text, 1)
    outname = input('Enter name of file to write verification : ')
    fout = open(outname, 'w')
    fout.write(str(signature[0]))
    fout.close()