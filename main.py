#!/usr/bin/env python3

# main.py
# Find the first word in a document with the maximum number of repetitions of
# any given letter.

import string   # For building the whitelist.

def main():
    pass

def repeatIndex(word):
    """ Return the number of times the most common letter in the word appears
        in the word. """
    word = word.lower()                 # Ignore capitalization.
    whitelist = string.ascii_lowercase  # Ignore punctuation.
    skip = []                           # Skip already counted letters.
    bestScore = 0
    for ch in word:
        if ch not in skip and ch in whitelist:
            skip += ch
            score = word.count(ch)
            if score > bestScore:
                bestScore = score
    return bestScore

"""
# test
teststr = "O Romeo, Romeo, wherefore art thou Romeo?"
for word in teststr.split(" "):
    print(repeatIndex(word))
"""

# (main trigger)
if __name__ = "__main__":
    main()
