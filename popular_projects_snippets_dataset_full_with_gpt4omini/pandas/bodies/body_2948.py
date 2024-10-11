# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame(
    {"A": [1, 2, np.nan, 4, 5, np.nan, 7], "C": [1, 2, 3, 5, 8, 13, 21]}
)
result = df.interpolate(method="barycentric")
expected = df.copy()
expected.loc[2, "A"] = 3
expected.loc[5, "A"] = 6
tm.assert_frame_equal(result, expected)

result = df.interpolate(method="barycentric", downcast="infer")
tm.assert_frame_equal(result, expected.astype(np.int64))

result = df.interpolate(method="krogh")
expectedk = df.copy()
expectedk["A"] = expected["A"]
tm.assert_frame_equal(result, expectedk)

result = df.interpolate(method="pchip")
expected.loc[2, "A"] = 3
expected.loc[5, "A"] = 6.0

tm.assert_frame_equal(result, expected)
