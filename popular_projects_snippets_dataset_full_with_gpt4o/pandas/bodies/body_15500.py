# Extracted from ./data/repos/pandas/pandas/tests/series/test_subclass.py
# https://github.com/pandas-dev/pandas/pull/34402
# allow subclass in both directions
s1 = pd.Series([1, 2, 3])
s2 = tm.SubclassedSeries([1, 2, 3])
assert s1.equals(s2)
assert s2.equals(s1)
