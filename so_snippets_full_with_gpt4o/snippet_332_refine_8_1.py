import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

DataFrame = type('Mock', (object,), {'values': np.random.random((1000, 100))}) # pragma: no cover
nd = np.random.random((1000, 100)) # pragma: no cover
df = pd.DataFrame(nd) # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

DataFrame = pd.DataFrame(np.random.random((1000, 100))) # pragma: no cover
nd = np.random.random((1000, 100)) # pragma: no cover
df = pd.DataFrame(nd) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
from l3.Runtime import _l_
np.random.shuffle(DataFrame.values)
_l_(12086)

nd = sklearn.utils.shuffle(nd)
_l_(12087)

np.random.shuffle(nd)
_l_(12088)

df = sklearn.utils.shuffle(df)
_l_(12089)

np.random.shuffle(df.values)
_l_(12090)
try:
    import timeit
    _l_(12092)

except ImportError:
    pass
setup = '''
import numpy as np
import pandas as pd
import sklearn
nd = np.random.random((1000, 100))
df = pd.DataFrame(nd)
'''
_l_(12093)

timeit.timeit('nd = sklearn.utils.shuffle(nd)', setup=setup, number=1000)
_l_(12094)
timeit.timeit('np.random.shuffle(nd)', setup=setup, number=1000)
_l_(12095)
timeit.timeit('df = sklearn.utils.shuffle(df)', setup=setup, number=1000)
_l_(12096)
timeit.timeit('np.random.shuffle(df.values)', setup=setup, number=1000)
_l_(12097)

