import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

df = pd.DataFrame({# pragma: no cover
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],# pragma: no cover
    'B': ['one', 'one', 'two', 'two', 'one', 'two', 'two', 'one'],# pragma: no cover
    'C': np.random.randn(8),# pragma: no cover
    'D': np.random.randn(8)# pragma: no cover
}) # pragma: no cover
grouper = 'A' # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

df = pd.DataFrame({# pragma: no cover
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],# pragma: no cover
    'B': ['one', 'one', 'two', 'two', 'one', 'two', 'two', 'one'],# pragma: no cover
    'C': np.random.randn(8),# pragma: no cover
    'D': np.random.randn(8)# pragma: no cover
})# pragma: no cover
# Defining additional methods to simulate a group object # pragma: no cover
class GroupMock:# pragma: no cover
    def __init__(self, name):# pragma: no cover
        self.name = name# pragma: no cover
    def sum(self):# pragma: no cover
        return 'sum'# pragma: no cover
Mock = type('Mock', (object,), {'groupby': lambda self, grouper, group_keys=False: df.groupby(grouper, group_keys=group_keys)}) # pragma: no cover
grouper = 'A' # pragma: no cover
df = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
from l3.Runtime import _l_
def f(group):
    _l_(19160)

    assert group.name is not None
    _l_(19158)
    aux = group
    _l_(19159)
    exit(aux)

def freduce(group):
    _l_(19163)

    assert group.name is not None
    _l_(19161)
    aux = group.sum()
    _l_(19162)
    exit(aux)

def freducex(x):
    _l_(19165)

    aux = freduce(x)
    _l_(19164)
    exit(aux)

grouped = df.groupby(grouper, group_keys=False)
_l_(19166)

# make sure all these work
grouped.apply(f)
_l_(19167)
grouped.aggregate(freduce)
_l_(19168)
grouped.aggregate({"C": freduce, "D": freduce})
_l_(19169)
grouped.transform(f)
_l_(19170)

grouped["C"].apply(f)
_l_(19171)
grouped["C"].aggregate(freduce)
_l_(19172)
grouped["C"].aggregate([freduce, freducex])
_l_(19173)
grouped["C"].transform(f)
_l_(19174)
