# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
float_frame["E"] = 1
assert issubclass(float_frame["E"].dtype.type, (int, np.integer))

result = float_frame.loc[float_frame.index[5], "E"]
assert is_integer(result)

# GH 11617
df = DataFrame({"a": [1.23]})
df["b"] = 666

result = df.loc[0, "b"]
assert is_integer(result)

expected = Series([666], [0], name="b")
result = df.loc[[0], "b"]
tm.assert_series_equal(result, expected)
