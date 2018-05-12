# A pangram is a sentence that contains every single letter of the alphabet at
# least once. For example, the sentence "The quick brown fox jumps over the lazy dog"
# is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
# Ignore numbers and punctuation.

import string

def is_pangram(str1, alphabet=string.ascii_lowercase):

    # Couldn't figure out how to do it by ignoring the numbers and punctuation,
    # instead opted to simply remove them from the given strings and work with
    # purely the letters instead.

    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
    for symbol in punctuation:
      str1 = str1.replace(symbol,"")

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for number in numbers:
      str1 = str1.replace(number, '')

    str1 = list(set(''.join(str1.lower().split(' '))))
    str1.sort()
    return (str1 == list(alphabet))

pangram = "The quick, brown fox jumps over the lazy dog!"
print is_pangram(pangram) # True
