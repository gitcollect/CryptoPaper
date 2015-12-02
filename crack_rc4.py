#!/usr/bin/env python
#
#     COURSE:  COMP 4140
# INSTRUCTOR:  Michael Zapp
# ASSIGNMENT:  Research Paper, RC4 Attack Implementation
#
#     USEAGE:  crack_rc4.py file_name

import argparse
import itertools
import time
import rc4
import string


def parse_args():
    parser = argparse.ArgumentParser(description='crack an rc4 encrypted file.')
    parser.add_argument('file_name', help='the file containing the ciphertext to be decrypted')
    args = parser.parse_args()

    return args


def gen_keys(alphabet, length):
    keys_generated = 0
    key_file = open('key_file.txt', 'w')
    print 'generating keys of up to length {0}'.format(length)
    write = key_file.write

    for n in range(1, length + 1):
        for x in itertools.product(alphabet, repeat=n):
            write(''.join(x) + '\n')
            keys_generated += 1

    print 'generated {0} keys'.format(keys_generated)

    key_file.close()


# Note: RC4 minimum key length of 40 bits (5 characters) ensures this is not
# really practical
def brute_force(ciphertext, plaintext):
    possibilities_tried = 0
    start = time.clock()

    with open('key_file.txt', 'r') as key_file:
        for possible_key in key_file:
            possible_key = possible_key.rstrip()
            print 'trying "{0}"'.format(possible_key)
            possibilities_tried += 1

            if rc4.encrypt(ciphertext,
                           possible_key) == plaintext:  # double encrypt
                print 'key found = "{0}"'.format(possible_key)
                break

    end = time.clock()
    print 'search took {0} seconds, tried {1} keys'.format((end - start),
                                                           possibilities_tried)


def main():
    # args = parse_args()

    # with open(args.file_name) as input_file:
    #     ciphertext = input_file.read()

    # key = 'Secret'
    # plaintext = 'Attack at dawn'

    key = 'Test'
    plaintext = 'something fun to try out'

    print 'Encrypting: "' + plaintext + '" with key "' + key + '"'
    data = rc4.encrypt(plaintext, key)

    # print 'Ciphertext: 0x' + ''.join(x.encode('hex') for x in data)
    # print 'Decrypting: returned "' + rc4.decrypt(data, key) + '" using
    # key "' + key + '"'

    alphabet = string.letters  # the legal key characters
    gen_keys(alphabet, 4)  # generate all possible keys, write to file
    brute_force(data, plaintext)  # really slow for key length > 4

# ===========================================================================run
if __name__ == '__main__':
    main()