# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
from l3.Runtime import _l_
mystring = 'Hello World, this should work!'
_l_(14969)
find_all = lambda c,s: [x for x in range(c.find(s), len(c)) if c[x] == s]
_l_(14970)

# s represents the search string
# c represents the character string

find_all(mystring,'o')    # will return all positions of 'o'
_l_(14971)    # will return all positions of 'o'

[4, 7, 20, 26] 
_l_(14972) 


