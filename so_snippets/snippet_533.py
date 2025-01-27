# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another
from l3.Runtime import _l_
set([1,2,6,8]).difference([2,3,5,8])
_l_(2800)
{1, 6}
_l_(2801)

l1, l2 = [1,2,6,8], [2,3,5,8]
_l_(2802)
s2 = set(l2)  # Type-cast `l2` to `set`
_l_(2803)  # Type-cast `l2` to `set`

l3 = [x for x in l1 if x not in s2]
_l_(2804)
                             #   ^ Doing membership checking on `set` s2

l1 = [1,2,6,8]
_l_(2805)
l2 = set([2,3,5,8])
_l_(2806)

#     v  `filter` returns the a iterator object. Here I'm type-casting 
#     v  it to `list` in order to display the resultant value
list(filter(lambda x: x not in l2, l1))
_l_(2807)
[1, 6]
_l_(2808)

