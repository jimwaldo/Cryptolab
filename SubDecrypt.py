#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:05:20 2018

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
    data = input('Enter string to decode : ')
    for i in range(1,len(l)):
        print (str(i), shift_string(data, i) )