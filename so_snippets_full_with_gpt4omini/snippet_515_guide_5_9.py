arr = [] # pragma: no cover
class MockList:  # Create a mock class to mimic the List's append behavior # pragma: no cover
    def __getitem__(self, index): # pragma: no cover
        if index == 0:  # Let's assume we have a successful mock for this example # pragma: no cover
            return lambda x: arr.append(x) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not
from l3.Runtime import _l_
arr = []
_l_(2527)
arr.append["HI"]
_l_(2528)

