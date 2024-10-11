import pandas as pd # pragma: no cover
from plydata import query # pragma: no cover

pandas = pd # pragma: no cover
query = query # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
from l3.Runtime import _l_
df = pandas.DataFrame({'foo': [1,2,15,17]})
_l_(1167)
y = 10
_l_(1168)
df >> query('foo > @y') # plydata
_l_(1169) # plydata
df.query('foo > @y') # pandas
_l_(1170) # pandas

