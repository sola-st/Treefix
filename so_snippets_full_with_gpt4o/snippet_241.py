# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
from l3.Runtime import _l_
x = [1, 2, 1, 3, 1, 4]
_l_(13907)

# brute force method
arr = []
_l_(13908)
for i in x:
  _l_(13911)

  if not i in arr:
    _l_(13910)

    arr.insert(x[i],i)
    _l_(13909)

# recursive method
tmp = []
_l_(13912)
def remove_duplicates(j=0):
  _l_(13918)

  if j < len(x):
    _l_(13917)

    if not x[j] in tmp:
      _l_(13914)

      tmp.append(x[j])
      _l_(13913)
    i = j+1  
    _l_(13915)  
    remove_duplicates(i)
    _l_(13916)

remove_duplicates()
_l_(13919)

