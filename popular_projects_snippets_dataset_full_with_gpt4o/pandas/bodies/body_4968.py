# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# https://github.com/pandas-dev/pandas/issues/33450
cat = Series(Categorical([np.nan], categories=[1, 2], ordered=True))
result = getattr(cat, function)(skipna=skipna)
assert result is np.nan
