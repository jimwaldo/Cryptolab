#!/usr/bin/env python
'''
Created on Oct 16, 2014

@author: waldo
'''
from Crypto.PublicKey import RSA
import pickle

if __name__ == '__main__':
    keyfile = input('Enter name of file containing key : ')
    f = open(keyfile, 'r')
    key = RSA.importKey(f.read())
    
    text = input('Enter text to encrypt : ')
    cypher_text = key.encrypt(bytes(text, 'utf8'), 1)
    print(cypher_text[0])

    fout_name = input('Enter name of a file to store the encrypted text : ')
    out_f = open(fout_name, 'wb')
    pickle.dump(cypher_text, out_f)
    out_f.close()