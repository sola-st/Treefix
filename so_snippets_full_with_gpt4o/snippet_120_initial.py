# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1747817/create-a-dictionary-with-comprehension
from l3.Runtime import _l_
names = ['a', 'b', 'd', 'f', 'c']
_l_(14318)
names_to_id = {v:k for k, v in enumerate(names)}
_l_(14319)
# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'f': 4}

names = ['a', 'b', 'd', 'f', 'd', 'c']
_l_(14320)
sorted_list = list(set(names))
_l_(14321)
sorted_list.sort()
_l_(14322)
names_to_id = {v:k for k, v in enumerate(sorted_list)}
_l_(14323)
# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'f': 4}

names = [1,2,5,5,6,2,1]
_l_(14324)
names_to_id = {v:k for k, v in enumerate(set(names))}
_l_(14325)
# {1: 0, 2: 1, 5: 2, 6: 3}

