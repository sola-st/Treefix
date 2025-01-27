# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
tz = tz_naive_fixture

dti = pd.date_range("2001-01-01", periods=11, tz=tz)
# shuffle so that we are not just working with monotone-increasing
dti = dti.take([4, 1, 3, 10, 9, 7, 8, 5, 0, 2, 6])
dtarr = dti._data

obj = box(dtarr)
assert obj.mean() == pd.Timestamp("2001-01-06", tz=tz)
assert obj.mean(skipna=False) == pd.Timestamp("2001-01-06", tz=tz)

# dtarr[-2] will be the first date 2001-01-1
dtarr[-2] = pd.NaT

obj = box(dtarr)
assert obj.mean() == pd.Timestamp("2001-01-06 07:12:00", tz=tz)
assert obj.mean(skipna=False) is pd.NaT
