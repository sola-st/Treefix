# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
from l3.Runtime import _l_
Base = ChildB
_l_(1378)

Base()
_l_(1379)

Base = ChildA
_l_(1380)

Base()
_l_(1381)

