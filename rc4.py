#!/usr/bin/env python
#
#       rc4.py - RC4, ARC4, ARCFOUR algorithm (with random salt removed)
#
#       Copyright (c) 2009 joonis new media
#       Author: Thimo Kraemer <thimo.kraemer@joonis.de>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#

__all__ = ['crypt', 'encrypt', 'decrypt']


def crypt(data, key):
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)


def encrypt(data, key):
    data = crypt(data, key)
    return data


def decrypt(data, key):
    return crypt(data, key)

if __name__ == '__main__':
    # test vectors verified using http://rc4.online-domain-tools.com/

    # ciphertext should be BBF316E8D940AF0AD3
    # key = 'Key'
    # plaintext = 'Plaintext'

    # ciphertext should be 1021BF0420
    # key = 'Wiki'
    # plaintext = 'pedia'

    # ciphertext should be 45A01F645FC35B383552544B9BF5
    key = 'Secret'
    plaintext = 'Attack at dawn'

    print 'Encrypting: "' + plaintext + '" with key "' + key + '"'
    data = encrypt(plaintext, key)

    print 'Ciphertext: 0x' + ''.join(x.encode('hex') for x in data)
    print 'Decrypting: returned "' + decrypt(data,
                                             key) + '" using key "' + key + '"'
