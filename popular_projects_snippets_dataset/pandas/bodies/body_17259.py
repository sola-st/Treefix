# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
df = DataFrame([[1, 2], [3, 4]])

result = methodcaller(func, "foo")(df)
assert df.index.name is None
assert result.index.name == "foo"

result = methodcaller(func, "cols", axis=1)(df)
assert df.columns.name is None
assert result.columns.name == "cols"
