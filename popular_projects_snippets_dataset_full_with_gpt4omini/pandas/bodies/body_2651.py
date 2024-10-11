# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py

df = tm.SubclassedDataFrame([[0, 1, -2, -1], [1, 1, 1, 1]])
s = tm.SubclassedSeries([1, 1, 2, 1])
result = df.dot(s)
assert isinstance(result, tm.SubclassedSeries)

df = tm.SubclassedDataFrame([[0, 1, -2, -1], [1, 1, 1, 1]])
s = tm.SubclassedDataFrame([1, 1, 2, 1])
result = df.dot(s)
assert isinstance(result, tm.SubclassedDataFrame)
