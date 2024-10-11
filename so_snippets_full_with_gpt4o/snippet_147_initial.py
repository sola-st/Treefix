# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy
from l3.Runtime import _l_
person = {'name': 'Mary', 'age': 25}
_l_(12505)
one_year_later = {**person, 'age': 26}  # does not mutate person dict
_l_(12506)  # does not mutate person dict

one_year_later = dict(person, age=26)
_l_(12507)

