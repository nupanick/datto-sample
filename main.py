#!/usr/bin/env python3

# main.py for datto-sample
# by Nicholas "nupanick" Lamicela
# September 2015

# Problem brief: Find the first word in a document with the maximum number of 
# repetitions of any individual letter.

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
                
                word = sanitize(word)
                score = repeatIndex(word)
                if score > bestScore:       # Reminder: first word wins ties.
                    bestWord = word
                    bestScore = score

            # Done reading word.
        # Done reading line.
    # Close file.

    # Announce the winning word.
    print(bestWord)
    return

def sanitize(word):
    """ Remove punctuation and capitalization from a word. """
    whitelist = string.ascii_lowercase  # Letters only.
    word = word.lower() 
    cleanWord = ''
    for ch in word:
        if ch in whitelist:
            cleanWord += ch
    return cleanWord


def repeatIndex(word):
    """ Return the number of times the most common letter in the word appears
        in the word. """
    skip = []               # Skip already counted letters.
    bestScore = 0
    for ch in word:
        if ch not in skip:
            skip += ch
            score = word.count(ch)
            if score > bestScore:
                bestScore = score
    return bestScore

# (main trigger)
if __name__ == "__main__":
    main()
