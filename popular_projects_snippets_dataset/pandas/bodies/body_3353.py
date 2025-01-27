# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# test case from
df = DataFrame(
    {"A": Series([3, 0], dtype="int64"), "B": Series([0, 3], dtype="int64")}
)
result = df.replace(3, df.mean().to_dict())
expected = df.copy().astype("float64")
m = df.mean()
expected.iloc[0, 0] = m[0]
expected.iloc[1, 1] = m[1]
tm.assert_frame_equal(result, expected)
