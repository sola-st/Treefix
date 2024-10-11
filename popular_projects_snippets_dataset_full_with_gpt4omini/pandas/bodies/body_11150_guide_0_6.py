import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

class MockGroup: # Mock implementation of the group object# pragma: no cover
    def __init__(self, name):# pragma: no cover
        self.name = name# pragma: no cover
    def sum(self):# pragma: no cover
        return 42# pragma: no cover
# pragma: no cover
grouper = 'A'# pragma: no cover
# Create a mock dataframe with groups# pragma: no cover
data = {'A': ['foo', 'bar', 'foo', 'bar'], 'C': [1, 2, 3, 4], 'D': [5, 6, 7, 8]}# pragma: no cover
df = pd.DataFrame(data)# pragma: no cover
df['A'] = df['A'].astype('category')# pragma: no cover
# Create a mock groupby object# pragma: no cover
class MockGroupBy:# pragma: no cover
    def __init__(self, df, grouper):# pragma: no cover
        self.df = df# pragma: no cover
        self.grouper = grouper# pragma: no cover
    def groupby(self, grouper, group_keys=False):# pragma: no cover
        return self# pragma: no cover
    def apply(self, func):# pragma: no cover
        return self.df.groupby(self.grouper).apply(func)# pragma: no cover
    def aggregate(self, func):# pragma: no cover
        return self.df.groupby(self.grouper).agg(func)# pragma: no cover
    def transform(self, func):# pragma: no cover
        return self.df.groupby(self.grouper).transform(func)# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return self.df[item]# pragma: no cover
# Instantiate MockGroupBy and assign to grouped# pragma: no cover
grouped = MockGroupBy(df, grouper) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
from l3.Runtime import _l_
def f(group):
    _l_(9000)

    assert group.name is not None
    _l_(8998)
    aux = group
    _l_(8999)
    exit(aux)

def freduce(group):
    _l_(9003)

    assert group.name is not None
    _l_(9001)
    aux = group.sum()
    _l_(9002)
    exit(aux)

def freducex(x):
    _l_(9005)

    aux = freduce(x)
    _l_(9004)
    exit(aux)

grouped = df.groupby(grouper, group_keys=False)
_l_(9006)

# make sure all these work
grouped.apply(f)
_l_(9007)
grouped.aggregate(freduce)
_l_(9008)
grouped.aggregate({"C": freduce, "D": freduce})
_l_(9009)
grouped.transform(f)
_l_(9010)

grouped["C"].apply(f)
_l_(9011)
grouped["C"].aggregate(freduce)
_l_(9012)
grouped["C"].aggregate([freduce, freducex])
_l_(9013)
grouped["C"].transform(f)
_l_(9014)
