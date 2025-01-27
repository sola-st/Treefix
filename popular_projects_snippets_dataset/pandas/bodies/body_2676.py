# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
# none
df = DataFrame(
    {
        "A": [None, None, "foo", "bar", "foo", "baz", "bar", "qux"],
        "C": [1.0, np.nan, np.nan, np.nan, 1.0, 2.0, 3, 1.0],
    }
)

# single column
result = df.drop_duplicates("A")
expected = df.iloc[[0, 2, 3, 5, 7]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates("A", keep="last")
expected = df.iloc[[1, 4, 5, 6, 7]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates("A", keep=False)
expected = df.iloc[[5, 7]]
tm.assert_frame_equal(result, expected)

# nan

# single column
result = df.drop_duplicates("C")
expected = df.iloc[[0, 1, 5, 6]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates("C", keep="last")
expected = df.iloc[[3, 5, 6, 7]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates("C", keep=False)
expected = df.iloc[[5, 6]]
tm.assert_frame_equal(result, expected)
