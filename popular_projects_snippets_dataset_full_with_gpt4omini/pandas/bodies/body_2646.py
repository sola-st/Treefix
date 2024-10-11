# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 25596

df = tm.SubclassedDataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
result = getattr(df, all_reductions)()
assert isinstance(result, tm.SubclassedSeries)
