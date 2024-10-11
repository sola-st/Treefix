# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/761804/how-do-i-trim-whitespace-from-a-string
from l3.Runtime import _l_
words=input("Enter the word to test")
_l_(13201)
# If I have a user enter discontinous threads it becomes a problem
# input = "   he llo, ho w are y ou  "
n=words.strip()
_l_(13202)
print(n)
_l_(13203)
# output "he llo, ho w are y ou" - only leading & trailing spaces are removed 

def whitespace(words):
    _l_(13207)

    r=words.replace(' ','') # removes all whitespace
    _l_(13204) # removes all whitespace
    n=r.replace(',','|') # other uses of replace
    _l_(13205) # other uses of replace
    aux = n
    _l_(13206)
    return aux
def run():
    _l_(13212)

    words=input("Enter the word to test") # take user input
    _l_(13208) # take user input
    m=whitespace(words) #encase the def in run() to imporve usability on various functions
    _l_(13209) #encase the def in run() to imporve usability on various functions
    o=m.count('f') # for testing
    _l_(13210) # for testing
    aux = m,o
    _l_(13211)
    return aux
print(run())
_l_(13213)
output- ('hello|howareyou', 0)
_l_(13214)

