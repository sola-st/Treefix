input = lambda prompt: '   he llo, ho w are y ou  ' # pragma: no cover
print = lambda x: x  # Mock print to display the output properly # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/761804/how-do-i-trim-whitespace-from-a-string
from l3.Runtime import _l_
words=input("Enter the word to test")
_l_(1577)
# If I have a user enter discontinous threads it becomes a problem
# input = "   he llo, ho w are y ou  "
n=words.strip()
_l_(1578)
print(n)
_l_(1579)
# output "he llo, ho w are y ou" - only leading & trailing spaces are removed 

def whitespace(words):
    _l_(1583)

    r=words.replace(' ','') # removes all whitespace
    _l_(1580) # removes all whitespace
    n=r.replace(',','|') # other uses of replace
    _l_(1581) # other uses of replace
    aux = n
    _l_(1582)
    return aux
def run():
    _l_(1588)

    words=input("Enter the word to test") # take user input
    _l_(1584) # take user input
    m=whitespace(words) #encase the def in run() to imporve usability on various functions
    _l_(1585) #encase the def in run() to imporve usability on various functions
    o=m.count('f') # for testing
    _l_(1586) # for testing
    aux = m,o
    _l_(1587)
    return aux
print(run())
_l_(1589)
output- ('hello|howareyou', 0)
_l_(1590)

