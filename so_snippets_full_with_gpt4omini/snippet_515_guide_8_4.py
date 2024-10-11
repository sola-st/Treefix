arr = [] # pragma: no cover
class MockList:  # Creating a mock class for simulating append functionality # pragma: no cover
    def __getitem__(self, index): # pragma: no cover
        if index == 0: # pragma: no cover
            return self.append_item # pragma: no cover
    def append_item(self, item): # pragma: no cover
        arr.append(item) # pragma: no cover
arr.append('HI') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not
from l3.Runtime import _l_
arr = []
_l_(2527)
arr.append["HI"]
_l_(2528)

