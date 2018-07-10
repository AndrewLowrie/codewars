# Complete the method/function so that it
# converts dash/underscore delimited words into camel
#  casing. The first word within the output should
#  be capitalized only if the original word was capitalized.

def to_camel_case(text):
    text = text.split('-').split('_')
    print(text)


to_camel_case('') # "An empty string was provided but not returned"
to_camel_case("the_stealth_warrior") # "theStealthWarrior"
