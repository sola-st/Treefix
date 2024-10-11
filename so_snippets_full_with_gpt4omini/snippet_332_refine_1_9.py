import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

nd = np.random.random((1000, 100)) # pragma: no cover
df = pd.DataFrame(nd) # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
np.random = np.random # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

nd = np.random.random((1000, 100)) # pragma: no cover
df = pd.DataFrame(nd) # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
sklearn = type('Mock', (object,), {'utils': type('MockUtils', (object,), {'shuffle': lambda x: np.random.permutation(x)})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
from l3.Runtime import _l_
np.random.shuffle(DataFrame.values)
_l_(154)

nd = sklearn.utils.shuffle(nd)
_l_(155)

np.random.shuffle(nd)
_l_(156)

df = sklearn.utils.shuffle(df)
_l_(157)

np.random.shuffle(df.values)
_l_(158)
try:
    import timeit
    _l_(160)

except ImportError:
    pass
setup = '''
import numpy as np
import pandas as pd
import sklearn
nd = np.random.random((1000, 100))
df = pd.DataFrame(nd)
'''
_l_(161)

timeit.timeit('nd = sklearn.utils.shuffle(nd)', setup=setup, number=1000)
_l_(162)
timeit.timeit('np.random.shuffle(nd)', setup=setup, number=1000)
_l_(163)
timeit.timeit('df = sklearn.utils.shuffle(df)', setup=setup, number=1000)
_l_(164)
timeit.timeit('np.random.shuffle(df.values)', setup=setup, number=1000)
_l_(165)

