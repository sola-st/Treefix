import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

data = {'dates': pd.date_range(start='1/1/2022', periods=10, freq='D'), 'values': np.random.randn(10)} # pragma: no cover
df = pd.DataFrame(data).set_index('dates') # pragma: no cover
def first(self, freq): # pragma: no cover
    return self.resample(freq).first() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/25254016/get-first-row-value-of-a-given-column
from l3.Runtime import _l_
x = df.first('d') # Returns the first day. '3d' gives first three days.
_l_(13858) # Returns the first day. '3d' gives first three days.

