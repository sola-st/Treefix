# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
# GH#24757
dti = pd.date_range("2001-01-01", periods=11)
# shuffle so that we are not just working with monotone-increasing
dti = dti.take([4, 1, 3, 10, 9, 7, 8, 5, 0, 2, 6])

parr = dti._data.to_period(freq)
obj = box(parr)
with pytest.raises(TypeError, match="ambiguous"):
    obj.mean()
with pytest.raises(TypeError, match="ambiguous"):
    obj.mean(skipna=True)

# parr[-2] will be the first date 2001-01-1
parr[-2] = pd.NaT

with pytest.raises(TypeError, match="ambiguous"):
    obj.mean()
with pytest.raises(TypeError, match="ambiguous"):
    obj.mean(skipna=True)
