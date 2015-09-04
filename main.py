#!/usr/bin/env python3

# main.py
# Find the first word in a document with the maximum number of repetitions of
# any given letter.

import string   # For building the whitelist.

teststr = "O Romeo, Romeo, wherefore art thou Romeo?"

# TODO: Change this loop to loop over words in a file instead of in a test
# string.

#for word in teststr.split(" ");

def repeatIndex(word):
    """ Return the number of times the most common letter in the word appears
        in the word. """
    word = word.lower()                 # Ignore capitalization.
    whitelist = string.ascii_lowercase  # Ignore punctuation.
    skip = []                           # Track already counted letters.
    bestScore = 0
    for ch in word:
        if ch not in skip and ch in whitelist:
            skip += ch
            score = word.count(ch)
            if score > bestScore:
                bestScore = score
    return bestScore

# test
for word in teststr.split(" "):
    print(repeatIndex(word))
