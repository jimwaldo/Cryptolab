#!/usr/bin/env python
'''
Created on Oct 16, 2014

@author: waldo
'''
from Crypto.PublicKey import RSA
import cPickle

if __name__ == '__main__':
    keyfile = input('Enter name of file containing decryption key : ')
    f = open(keyfile, 'r')
    key = RSA.importKey(f.read())
    
    fname = input('Enter file name containing encrypted text : ')
    fin = open(fname, 'rb')
    text = cPickle.load(fin)
    plain_text = key.decrypt(text)
    print(plain_text)

