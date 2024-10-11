# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
from l3.Runtime import _l_
x = [1, 2, 1, 3, 1, 4]
_l_(1655)

# brute force method
arr = []
_l_(1656)
for i in x:
  _l_(1659)

  if not i in arr:
    _l_(1658)

    arr.insert(x[i],i)
    _l_(1657)

# recursive method
tmp = []
_l_(1660)
def remove_duplicates(j=0):
  _l_(1666)

  if j < len(x):
    _l_(1665)

    if not x[j] in tmp:
      _l_(1662)

      tmp.append(x[j])
      _l_(1661)
    i = j+1  
    _l_(1663)  
    remove_duplicates(i)
    _l_(1664)

remove_duplicates()
_l_(1667)

