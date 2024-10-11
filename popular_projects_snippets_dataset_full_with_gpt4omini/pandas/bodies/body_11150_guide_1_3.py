import pandas as pd # pragma: no cover

data = {'A': [1, 1, 2, 2], 'C': [10, 20, 30, 40], 'D': [50, 60, 70, 80]} # pragma: no cover
df = pd.DataFrame(data) # pragma: no cover
grouper = 'A' # pragma: no cover
class MockGroup:  # Creating a mock group class# pragma: no cover
    def __init__(self, name, values):# pragma: no cover
        self.name = name# pragma: no cover
        self.values = values# pragma: no cover
    def sum(self):# pragma: no cover
        return sum(self.values)# pragma: no cover
# pragma: no cover
# Creating a mock series of groups# pragma: no cover
mocked_groups = [MockGroup(name, df[df['A'] == name]['C'].tolist()) for name in df['A'].unique()] # pragma: no cover
class MockGroupBy:# pragma: no cover
    def __init__(self, groups):# pragma: no cover
        self.groups = groups# pragma: no cover
    def apply(self, func):# pragma: no cover
        return [func(g) for g in self.groups]# pragma: no cover
    def aggregate(self, func):# pragma: no cover
        return [func(g) for g in self.groups]# pragma: no cover
    def transform(self, func):# pragma: no cover
        return [func(g) for g in self.groups]# pragma: no cover
# pragma: no cover
# Instantiate the mock groupby object# pragma: no cover
grouped = MockGroupBy(mocked_groups) # pragma: no cover

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
