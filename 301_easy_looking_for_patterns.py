"""Description

You will be given a sequence that of letters and you must match with a
dictionary. The sequence is a pattern of equal letters that you must find.
E.G.
Pattern:
XXYY means that you have a word that contains a sequence of 2 of the same
letters followed by again 2 of the same letters.

succeed <- matches
succes <- no match

XYYX means we have a word with at least for letters where you have a sequence
of a letter, followed by 2 letters that are the same and then again the first
letter.

narrate <- matches
hodor <- no match"""

import re
import urllib.request

def distinct_letter(n):
    if (n == 0):
        return '(\w)'
    else:
        return '(?=(?!\{0}))'.format(n) + distinct_letter(n-1)

def pattern_builder(sequence):
    list_of_letters = []
    pattern = ''

    for letter in sequence:
        if letter not in list_of_letters:
            list_of_letters.append(letter)
            pattern += distinct_letter(list_of_letters.index(letter))
        else:
            pattern += '\{0}'.format(list_of_letters.index(letter) + 1)

    return pattern

def looking_for_patterns(sequence):
    pattern = re.compile(pattern_builder(sequence))

    dictionary = urllib.request.urlopen(
        'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt')\
        .read()\
        .decode('utf8')\
        .split('\n')

    for word in dictionary:
        if re.search(pattern, word):
            print(word)

looking_for_patterns('XXYYZZ')