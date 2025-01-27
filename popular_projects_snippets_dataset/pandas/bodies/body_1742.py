# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
dti = date_range(
    start=datetime(2005, 1, 1), end=datetime(2005, 1, 10), freq="D"
).as_unit(unit)
s = Series(np.random.rand(len(dti)), dti)
bs = s.resample("B", closed="right", label="right").mean()
result = bs.resample("8H").mean()
assert len(result) == 22
assert isinstance(result.index.freq, offsets.DateOffset)
assert result.index.freq == offsets.Hour(8)
