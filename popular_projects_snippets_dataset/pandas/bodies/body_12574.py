# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
vals = [
    [10, 1, "foo", 0.1, 0.01],
    [20, 2, "bar", 0.2, 0.02],
    [30, 3, "baz", 0.3, 0.03],
    [40, 4, "qux", 0.4, 0.04],
]

df = DataFrame(
    vals, index=list("abcd"), columns=["1st", "2nd", "3rd", "4th", "5th"]
)

assert df._is_mixed_type
right = df.copy()

for orient in ["split", "index", "columns"]:
    inp = df.to_json(orient=orient)
    left = read_json(inp, orient=orient, convert_axes=False)
    tm.assert_frame_equal(left, right)

right.index = pd.RangeIndex(len(df))
inp = df.to_json(orient="records")
left = read_json(inp, orient="records", convert_axes=False)
tm.assert_frame_equal(left, right)

right.columns = pd.RangeIndex(df.shape[1])
inp = df.to_json(orient="values")
left = read_json(inp, orient="values", convert_axes=False)
tm.assert_frame_equal(left, right)
