# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
orig = DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "bar", "foo"],
        "B": ["one", "one", "two", "two", "two", "two", "one", "two"],
        "C": [1, 1, 2, 2, 2, 2, 1, 2],
        "D": range(8),
    }
)
# single column
df = orig.copy()
return_value = df.drop_duplicates("A", inplace=True)
expected = orig[:2]
result = df
tm.assert_frame_equal(result, expected)
assert return_value is None

df = orig.copy()
return_value = df.drop_duplicates("A", keep="last", inplace=True)
expected = orig.loc[[6, 7]]
result = df
tm.assert_frame_equal(result, expected)
assert return_value is None

df = orig.copy()
return_value = df.drop_duplicates("A", keep=False, inplace=True)
expected = orig.loc[[]]
result = df
tm.assert_frame_equal(result, expected)
assert len(df) == 0
assert return_value is None

# multi column
df = orig.copy()
return_value = df.drop_duplicates(["A", "B"], inplace=True)
expected = orig.loc[[0, 1, 2, 3]]
result = df
tm.assert_frame_equal(result, expected)
assert return_value is None

df = orig.copy()
return_value = df.drop_duplicates(["A", "B"], keep="last", inplace=True)
expected = orig.loc[[0, 5, 6, 7]]
result = df
tm.assert_frame_equal(result, expected)
assert return_value is None

df = orig.copy()
return_value = df.drop_duplicates(["A", "B"], keep=False, inplace=True)
expected = orig.loc[[0]]
result = df
tm.assert_frame_equal(result, expected)
assert return_value is None

# consider everything
orig2 = orig.loc[:, ["A", "B", "C"]].copy()

df2 = orig2.copy()
return_value = df2.drop_duplicates(inplace=True)
# in this case only
expected = orig2.drop_duplicates(["A", "B"])
result = df2
tm.assert_frame_equal(result, expected)
assert return_value is None

df2 = orig2.copy()
return_value = df2.drop_duplicates(keep="last", inplace=True)
expected = orig2.drop_duplicates(["A", "B"], keep="last")
result = df2
tm.assert_frame_equal(result, expected)
assert return_value is None

df2 = orig2.copy()
return_value = df2.drop_duplicates(keep=False, inplace=True)
expected = orig2.drop_duplicates(["A", "B"], keep=False)
result = df2
tm.assert_frame_equal(result, expected)
assert return_value is None
