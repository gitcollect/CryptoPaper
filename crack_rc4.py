#!/usr/bin/env python
#
#     COURSE:  COMP 4140
# INSTRUCTOR:  Michael Zapp
# ASSIGNMENT:  Research Paper, RC4 Attack Implementation
#
#     USEAGE:  crack_rc4.py file_name

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='crack an rc4 encrypted file.')
    parser.add_argument('file_name', help='the file containing the ciphertext to be decrypted')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    with open(args.file_name) as input_file:
        ciphertext = input_file.read()

# ===========================================================================run
if __name__ == '__main__':
    main()