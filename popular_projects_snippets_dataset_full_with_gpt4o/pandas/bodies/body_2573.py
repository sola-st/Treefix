# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#2155
columns = date_range(start="1/1/2012", end="2/1/2012", freq=BDay())
data = DataFrame(columns=columns, index=range(10))
t = datetime(2012, 11, 1)
ts = Timestamp(t)
data[ts] = np.nan  # works, mostly a smoke-test
assert np.isnan(data[ts]).all()
