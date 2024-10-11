import pandas as pd # pragma: no cover

data = {'A': [1, 1, 2, 2], 'B': [5, 6, 7, 8], 'C': [1, 2, 3, 4], 'D': [10, 20, 30, 40]} # pragma: no cover
df = pd.DataFrame(data) # pragma: no cover
grouper = 'A' # pragma: no cover
class MockGroup:  # Mock class to simulate a grouped DataFrame object # pragma: no cover
    def __init__(self, name, data): # pragma: no cover
        self.name = name # pragma: no cover
        self.data = data # pragma: no cover
    def sum(self): # pragma: no cover
        return self.data['C'].sum() # pragma: no cover
mocked_groups = [MockGroup(name, group) for name, group in df.groupby(grouper)] # pragma: no cover
class MockGroupBy:  # Mock object to replace DataFrame groupby behavior # pragma: no cover
    def __init__(self, df): # pragma: no cover
        self.df = df # pragma: no cover
    def groupby(self, grouper, group_keys=False): # pragma: no cover
        return [MockGroup(name, group) for name, group in self.df.groupby(grouper)] # pragma: no cover
grouped = MockGroupBy(df).groupby(grouper) # pragma: no cover

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
