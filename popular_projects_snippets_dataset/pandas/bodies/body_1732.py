# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# from daily
dti = date_range(
    start=datetime(2005, 1, 1), end=datetime(2005, 1, 10), freq="D", name="index"
).as_unit(unit)

s = Series(np.random.rand(len(dti)), dti)

# to minutely, by padding
result = s.resample("Min").ffill()
assert len(result) == 12961
assert result[0] == s[0]
assert result[-1] == s[-1]

assert result.index.name == "index"
