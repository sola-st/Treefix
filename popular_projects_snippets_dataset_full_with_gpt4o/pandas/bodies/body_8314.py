# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
from pandas import DateOffset

index_1 = date_range("1/1/2012", periods=4, freq="12H")
index_2 = index_1 + DateOffset(hours=1)

result = index_1.intersection(index_2)
assert len(result) == 0
