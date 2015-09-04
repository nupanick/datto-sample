#!/usr/bin/env python3

# main.py
# Find the first word in a document with the maximum number of repetitions of
# any given letter.

import sys      # For the command line argument.
import string   # For building the whitelist.

def main():
    """ Read in a text file and print out the word with the highest
        repeatIndex() score. """
    
    # Get filename from args
    if not len(sys.argv) == 2:
        print("Usage: " + sys[0] + "<input file>")
        return
    filename = sys.argv[1]

    # Read file line by line, word by word, looking for the best score.
    bestWord = ""
    bestScore = 0

    # Open file.
    with open(filename) as f:
        # Read line.
        for line in f.readlines():
            # Read word.
            for word in line.split(" "):
                # Word-by-word logic goes here.
                
                print(word)

            # Done reading word.
        # Done reading line.
    # Close file.

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
if __name__ == "__main__":
    main()
