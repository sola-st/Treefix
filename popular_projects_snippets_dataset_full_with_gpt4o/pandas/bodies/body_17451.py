# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH#34511
off = DateOffset(months=12)
res = tm.round_trip_pickle(off)
assert off == res

base_dt = datetime(2020, 1, 1)
assert base_dt + off == base_dt + res
