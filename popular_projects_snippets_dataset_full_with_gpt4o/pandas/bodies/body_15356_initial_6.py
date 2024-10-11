import pandas as pd # pragma: no cover

string_series = pd.Series(['a', 'b', 'c', 'd'], index=[0, 1, 2, 3]) # pragma: no cover
object_series = pd.Series([{ 'key1': 'value1'}, { 'key2': 'value2'}, { 'key3': 'value3'}, { 'key4': 'value4'}], index=[0, 1, 2, 3]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
from l3.Runtime import _l_
slice1 = string_series[[1, 2, 3]]
_l_(15894)
slice2 = object_series[[1, 2, 3]]
_l_(15895)
assert string_series.index[2] == slice1.index[1]
_l_(15896)
assert object_series.index[2] == slice2.index[1]
_l_(15897)
assert string_series[2] == slice1[1]
_l_(15898)
assert object_series[2] == slice2[1]
_l_(15899)
