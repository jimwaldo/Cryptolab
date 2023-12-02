from Crypto.Hash import SHA256
import time, sys

def find_zero_hash(in_str, num_zeros):
    comp_str = ''
    for i in range(0, num_zeros):
        comp_str = comp_str + '0'
    i = 0
    p = str(i) + in_str
    hash_f = SHA256.new()
    hash_f.update(bytes(p, 'utf8'))
    hp = hash_f.hexdigest()
    now = time.time()
    while (hp[:num_zeros] != comp_str):
        i += 1
        p = str(i) + in_str
        hash_f.update(bytes(p, 'utf8'))
        hp = hash_f.hexdigest()
    then = time.time()
    return then - now, i

if __name__ == '__main__':
    if len(sys.argv) < 3:
        in_str = input('Enter string to hash : ')
        num_zeros = int(input('Enter number of leading zeros : '))
    else:
        in_str = sys.argv[1]
        num_zeros = int(sys.argv[2])

    calc_time, calc_iters = find_zero_hash(in_str, num_zeros)
    print('time to find hash = ' +  str(calc_time))
    print('iterations to find hash = ' +  str(calc_iters))