# Extracted from ./data/repos/pandas/pandas/tests/frame/test_cumulative.py
# GH#19296 dont incorrectly upcast to object
df = DataFrame({"A": [1, 2, 3], "B": [1, 2, 3.0], "C": [True, False, False]})

result = df.cumsum()

expected = DataFrame(
    {
        "A": Series([1, 3, 6], dtype=np.int64),
        "B": Series([1, 3, 6], dtype=np.float64),
        "C": df["C"].cumsum(),
    }
)
tm.assert_frame_equal(result, expected)
