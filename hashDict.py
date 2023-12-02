
import hashlib
import time
import pickle

if __name__ == '__main__':
    start = time.time()
    fin = open('/usr/share/dict/words', 'r')
    hashdict = {}
    wordhash = {}
    for l in fin:
        w = l[:-1]
        h = hashlib.md5(bytearray(w,'utf8')).hexdigest()
        hashdict[h] = w
        wordhash[w] = h

    end = time.time()
    pickle.dump(hashdict, open('hashToWord.pkl', 'bw'))
    pickle.dump(wordhash, open('wordToHash.pkl', 'bw'))
    print('number of items hashed =' + str(len(hashdict)))
    print('time to hash = ' + str(end - start))
