# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1894269/how-to-convert-string-representation-of-list-to-a-list
from l3.Runtime import _l_
x = '[ "A","B","C" , " D"]'
_l_(13700)
[i.strip() for i in x.split('"') if len(i.strip().strip(',').strip(']').strip('['))>0]
_l_(13701)

['A', 'B', 'C', 'D']
_l_(13702)

