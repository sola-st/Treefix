# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py

# int block splitting
df = DataFrame(
    {
        "A": Series([1.0, 2.0], dtype="float64"),
        "B": Series([0, 1], dtype="int64"),
        "C": Series([1, 2], dtype="int64"),
    }
)
expected = DataFrame(
    {
        "A": Series([1.0, 2.0], dtype="float64"),
        "B": Series([0.5, 1], dtype="float64"),
        "C": Series([1, 2], dtype="int64"),
    }
)
result = df.replace(0, 0.5)
tm.assert_frame_equal(result, expected)
