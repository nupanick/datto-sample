#!/usr/bin/env python3

# main.py
# Find the first word in a document with the maximum number of repetitions of
# any given letter.

from string import ascii_lowercase as whitelist     # For avoiding punctuation

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
            cleanword += ch
    return cleanword

def repeatIndex(word):
    """ Return the number of times the most common letter in the word appears
        in the word. """
    word = sanitize(word)   # Ignore capitalization and punctuation
    skip = []               # Track already counted letters
    bestScore = 0
    for ch in word:
        if ch not in skip:
            skip += ch
            score = word.count(ch)
            if score > bestScore:
                bestScore = score
    return bestScore

# test
for word in teststr.split(" "):
    print(repeatIndex(word))
