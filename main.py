#!/usr/bin/env python3

# main.py
# Find the first word in a document with the maximum number of repetitions of
# any given letter.

import string.ascii_lowercase as whitelist      # For avoiding punctuation

teststr = "O Romeo, Romeo, wherefore art thou Romeo?"

# TODO: Change this loop to loop over words in a file instead of in a test
# string.

#for word in teststr.split(" ");


def sanitize(word):
    """ Convert letters to lowercase, and remove everything else. """
    word = str.lower(word)
    cleanword = ''
    for ch in word:
        if ch in whitelist:
            cleanword.join(ch)
    return cleanword

def repeatIndex():
    print("Hello World")
    return

