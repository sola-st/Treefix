# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 8238
# all nan
vals = Series([np.nan] * 10)
result = vals.rolling(5, center=True, win_type="boxcar", step=step).mean()
assert np.isnan(result).all()

# empty
vals = Series([], dtype=object)
result = vals.rolling(5, center=True, win_type="boxcar", step=step).mean()
assert len(result) == 0

# shorter than window
vals = Series(np.random.randn(5))
result = vals.rolling(10, win_type="boxcar", step=step).mean()
assert np.isnan(result).all()
assert len(result) == len(range(0, 5, step or 1))
