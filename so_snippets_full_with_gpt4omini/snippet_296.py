# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1894269/how-to-convert-string-representation-of-list-to-a-list
from l3.Runtime import _l_
x = '[ "A","B","C" , " D"]'
_l_(2265)
[i.strip() for i in x.split('"') if len(i.strip().strip(',').strip(']').strip('['))>0]
_l_(2266)

['A', 'B', 'C', 'D']
_l_(2267)

