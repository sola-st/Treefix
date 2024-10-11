class MockAppend: # pragma: no cover
    def __getitem__(self, item): # pragma: no cover
        print(f'Item accessed with key: {item}') # pragma: no cover
arr = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not
from l3.Runtime import _l_
arr = []
_l_(14284)
arr.append["HI"]
_l_(14285)

