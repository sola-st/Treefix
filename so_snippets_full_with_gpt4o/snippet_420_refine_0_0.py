import pandas as pd # pragma: no cover

data = {'A': [0.13200317033032932], 'B': [1.23], 'C': [4.56]} # pragma: no cover
index = ['a'] # pragma: no cover
df1 = pd.DataFrame(data, index=index) # pragma: no cover

import pandas as pd # pragma: no cover

data = {'A': [0.13200317033032932], 'B': [1.23], 'C': [4.56]} # pragma: no cover
index = ['a'] # pragma: no cover
df1 = pd.DataFrame(data, index=index) # pragma: no cover
In = type('Mock', (object,), {'55': df1.loc['a', 'A']}) # pragma: no cover
Out = type('Mock', (object,), {'55': 0.13200317033032932}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16729574/how-can-i-get-a-value-from-a-cell-of-a-dataframe
# This is also equivalent to df1.at['a','A']
from l3.Runtime import _l_
In [55]: df1.loc['a', 'A']
_l_(11962)
Out[55]: 0.13200317033032932
_l_(11963)

