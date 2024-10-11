# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
df = DataFrame(
    {
        "AAA": ["foo", "bar", "baz", "bar", "foo", "bar", "qux", "foo"],
        "B": ["one", "one", "two", "two", "two", "two", "one", "two"],
        "C": [1, 1, 2, 2, 2, 2, 1, 2],
        "D": range(8),
    }
)
# single column
result = df.drop_duplicates("AAA")
expected = df.iloc[[0, 1, 2, 6]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates("AAA", keep="last")
expected = df.iloc[[2, 5, 6, 7]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates("AAA", keep=False)
expected = df.iloc[[2, 6]]
tm.assert_frame_equal(result, expected)

# multiple columns
result = df.drop_duplicates(["AAA", "B"])
expected = df.iloc[[0, 1, 2, 3, 4, 6]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates(["AAA", "B"], keep="last")
expected = df.iloc[[0, 1, 2, 5, 6, 7]]
tm.assert_frame_equal(result, expected)

result = df.drop_duplicates(["AAA", "B"], keep=False)
expected = df.iloc[[0, 1, 2, 6]]
tm.assert_frame_equal(result, expected)
