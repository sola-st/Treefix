# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
str(string_series)
str(string_series.astype(int))

# with NaNs
string_series[5:7] = np.NaN
str(string_series)
