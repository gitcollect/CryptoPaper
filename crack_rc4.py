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
import os


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


def weakKeyDistribution():
    keys = generateKeys()

    B = 0
    IV = {B + 3, 0xf, 0x7}
    SK = {1, 2, 3, 4, 5}
    K = IV + SK
    l = len(K)


def getDistribution(keys):
    dist = [0] * 256
    count = 0

    for key in keys:
        # create random plain text and apply one of the keys to it
        data = os.urandom(47)
        data.encode('base-64')
        keyString = str(key)
        ciphertext = rc4.crypt(data, keyString)

        # print key[0]
        # print key[1]
        # print key[2]
        # print ord(ciphertext[0])

        dist[ord(ciphertext[0]) - key[2]] += 1
        count += 1

    showProbabilities(dist, count)


def showProbabilities(dist, count):
    print count
    for i in range(256):
        print "Probability that K[2] + %i = B[0] is %.8f%%" % (i, ((dist[i] / (count + 0.0))*100))


def generateKeys():
    print "Generating Keys"

    keys = []

    for k in range(7, 15):

        key = bytearray(k)

        for i in range(256):

            key[0] = i
            key[1] = (256 - i) % 256

            for j in range(2, k):
                key[j] = os.urandom(1)

            keys.append(key)
            #print ''.join('{:02x}'.format(x) for x in key)

    return keys


def main():
    # args = parse_args()

    # with open(args.file_name) as input_file:
    #     ciphertext = input_file.read()

    getDistribution(generateKeys())

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
    # brute_force(data, plaintext)  # really slow for key length > 4


# ===========================================================================run
if __name__ == '__main__':
    main()
