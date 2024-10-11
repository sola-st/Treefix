# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
ts1 = tm.makeTimeSeries()
ts2 = tm.makeTimeSeries()[::2]

# to join with union
# these two are of different length!
left = concat([ts1, ts2], join="outer", axis=1)
right = concat([ts2, ts1], join="outer", axis=1)

assert len(left) == len(right)
