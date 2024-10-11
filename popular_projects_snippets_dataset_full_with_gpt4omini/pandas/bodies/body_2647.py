# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py

df = tm.SubclassedDataFrame(
    {
        "Person": ["John", "Myla", "Lewis", "John", "Myla"],
        "Age": [24.0, np.nan, 21.0, 33, 26],
        "Single": [False, True, True, True, False],
    }
)
result = df.count()
assert isinstance(result, tm.SubclassedSeries)

df = tm.SubclassedDataFrame({"A": [1, 0, 3], "B": [0, 5, 6], "C": [7, 8, 0]})
result = df.count()
assert isinstance(result, tm.SubclassedSeries)

df = tm.SubclassedDataFrame(
    [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]],
    index=MultiIndex.from_tuples(
        list(zip(list("AABB"), list("cdcd"))), names=["aaa", "ccc"]
    ),
    columns=MultiIndex.from_tuples(
        list(zip(list("WWXX"), list("yzyz"))), names=["www", "yyy"]
    ),
)
result = df.count()
assert isinstance(result, tm.SubclassedSeries)

df = tm.SubclassedDataFrame()
result = df.count()
assert isinstance(result, tm.SubclassedSeries)
