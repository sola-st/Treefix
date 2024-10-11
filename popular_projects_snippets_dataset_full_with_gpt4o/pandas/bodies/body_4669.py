# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
samples = np.hstack([samples, np.nan])
skew = nanops.nanskew(samples, skipna=False)
assert np.isnan(skew)
