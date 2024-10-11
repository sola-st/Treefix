# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# 2252
t1 = Timestamp((1352934390 * 1000000000) + 1000000 + 1000 + 1)
idx = DatetimeIndex([t1])

assert idx.nanosecond[0] == t1.nanosecond
