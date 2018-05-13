# ROT13 is a simple letter substitution cipher that replaces a letter with
# the letter 13 letters after it in the alphabet. ROT13 is an example of
# the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered
# with Rot13. If there are numbers or special characters included in the
# string, they should be returned as they are. Only letters from the
# latin/english alphabet should be shifted, like in the original
# Rot13 "implementation".
#
# Please note that using "encode" in Python is considered cheating.

import string
from codecs import encode as _dont_use_this_

def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_shifted = alphabet[13:] + alphabet[:13]

    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_shifted2 = alphabet2[13:] + alphabet2[:13]

    translate_table = string.maketrans(alphabet, alphabet_shifted)
    message = message.translate(translate_table)

    translate_table2 = string.maketrans(alphabet2, alphabet_shifted2)
    message = message.translate(translate_table2)

    return message

print(rot13("test"))
# "grfg"
print(rot13("Test"))
# "Grfg"
