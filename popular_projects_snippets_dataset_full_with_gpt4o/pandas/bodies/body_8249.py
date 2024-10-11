# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
rng = date_range(START, END, freq=pd.offsets.BMonthEnd())
shifted = rng.shift(1, freq=pd.offsets.BDay())
assert shifted[0] == rng[0] + pd.offsets.BDay()

rng = date_range(START, END, freq=pd.offsets.BMonthEnd())
with tm.assert_produces_warning(pd.errors.PerformanceWarning):
    shifted = rng.shift(1, freq=pd.offsets.CDay())
    assert shifted[0] == rng[0] + pd.offsets.CDay()
