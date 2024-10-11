# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
# see gh-6129: new columns
df = DataFrame({"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}})
row = Series([5, 6, 7], index=["a", "b", "c"], name="z")
expected = DataFrame(
    {
        "a": {"x": 1, "y": 2, "z": 5},
        "b": {"x": 3, "y": 4, "z": 6},
        "c": {"z": 7},
    }
)
result = df._append(row)
tm.assert_frame_equal(result, expected)
