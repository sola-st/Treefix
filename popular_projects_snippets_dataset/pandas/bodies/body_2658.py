# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH#40810
df = tm.SubclassedDataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

result = df.astype({"A": np.int64, "B": np.int32, "C": np.float64})
assert isinstance(result, tm.SubclassedDataFrame)
