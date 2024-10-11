# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
# GH21012

index = date_range("2000-01-01 00:00:00", periods=periods, freq="min")
num = 0
for stamp in index:
    assert index[num] == stamp
    num += 1
assert num == len(index)
