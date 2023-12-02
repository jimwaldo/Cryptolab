#!/usr/bin/env python

import hashlib

if __name__ == '__main__':
    d = input('Enter text to hash : ')
    hash = hashlib.new('SHA256')
    hash.update(bytes(d, 'utf8'))
    print(hash.hexdigest())
