# Extracted from ./data/repos/pandas/pandas/tests/series/test_subclass.py
s = tm.SubclassedSeries([[1, 2, 3], "foo", [], [3, 4]])
result = s.explode()
assert isinstance(result, tm.SubclassedSeries)
