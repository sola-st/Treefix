import pandas # pragma: no cover
from plydata import query # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
from l3.Runtime import _l_
df = pandas.DataFrame({'foo': [1,2,15,17]})
_l_(13591)
y = 10
_l_(13592)
df >> query('foo > @y') # plydata
_l_(13593) # plydata
df.query('foo > @y') # pandas
_l_(13594) # pandas

