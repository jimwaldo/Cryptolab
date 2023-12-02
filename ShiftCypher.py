#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:09:20 2018

@author: waldo
"""
import string

l = list(string.ascii_letters)

def shift_string(st_in, shift):
    ret_str = ''
    for c in st_in:
        if c in l:
            i = l.index(c)
            sh_i = (i + shift) % len(l)
            ret_str += l[sh_i]
        else:
            ret_str += c
    return ret_str

if __name__ == '__main__':
    data = input('Enter string to encode : ')
    shift_size = int(input('Enter rotation : '))
    
    shift_d = shift_string(data, shift_size)
    print(shift_d)