# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
df = DataFrame(
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    columns=["A", "B", "C", "D"],
    index=Index(range(2), name="x"),
)
assert df.reset_index().index.name is None
assert df.reset_index(drop=True).index.name is None
return_value = df.reset_index(inplace=True)
assert return_value is None
assert df.index.name is None
