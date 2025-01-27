# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# GH
df = DataFrame(
    {
        "A": [1, 2, np.nan, 4],
        "B": [1, 2, 3, 4],
        "C": [1.0, 2.0, np.nan, 4.0],
        "D": [1.0, 2.0, 3.0, 4.0],
    }
)
expected = DataFrame(
    {
        "A": np.array([1, 2, 3, 4], dtype="float64"),
        "B": np.array([1, 2, 3, 4], dtype="int64"),
        "C": np.array([1.0, 2.0, 3, 4.0], dtype="float64"),
        "D": np.array([1.0, 2.0, 3.0, 4.0], dtype="float64"),
    }
)

result = df.interpolate(downcast=None)
tm.assert_frame_equal(result, expected)

# all good
result = df[["B", "D"]].interpolate(downcast=None)
tm.assert_frame_equal(result, df[["B", "D"]])
