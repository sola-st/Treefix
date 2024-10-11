# Extracted from ./data/repos/pandas/pandas/tests/base/test_unique.py
obj = index_or_series_obj
obj = np.repeat(obj, range(1, len(obj) + 1))
expected = len(obj.unique())
assert obj.nunique(dropna=False) == expected
