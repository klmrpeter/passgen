#!/usr/bin/env python3

import string
import random
import argparse

def passgen(size=0, chars="", numbers=False, specials=False, lowercase=False, uppercase=False):

    if numbers:
        chars += string.digits

    if specials:
        chars += string.punctuation

    if lowercase:
        chars += string.ascii_lowercase

    if uppercase:
        chars += string.ascii_uppercase
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

if __name__ == "__main__":
    size = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int)
    parser.add_argument("-f", "--numbers", action="store_true")
    parser.add_argument("-u", "--specials", action="store_true")
    parser.add_argument("-c", "--lowercase", action="store_true")
    parser.add_argument("-k", "--uppercase", action="store_true")

    args = parser.parse_args()
    if args.size:
        size = args.size


    print(passgen(size=size, numbers=args.numbers, specials=args.specials, lowercase=args.lowercase, uppercase=args.uppercase))
