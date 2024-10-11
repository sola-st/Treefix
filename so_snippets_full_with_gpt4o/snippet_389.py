# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
from l3.Runtime import _l_
for item in sequence:
    _l_(12552)

    process(item)
    _l_(12550)
else:  # no break
    suite
    _l_(12551)

