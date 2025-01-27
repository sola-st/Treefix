# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py
# GH 18430
s = Series(np.zeros(20))
other = Series(np.arange(20))

assert s.rolling(window=window).corr(other=other).isna().all()
