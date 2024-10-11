# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
frame = DataFrame(
    np.random.randn(4, 4), index=[1, 2, 3, 4], columns=["A", "B", "C", "D"]
)

# axis=0
unordered = frame.loc[[3, 2, 4, 1]]
a_values = unordered["A"]
df = unordered.copy()
return_value = df.sort_index(inplace=True)
assert return_value is None
expected = frame
tm.assert_frame_equal(df, expected)
# GH 44153 related
# Used to be a_id != id(df["A"]), but flaky in the CI
assert a_values is not df["A"]

df = unordered.copy()
return_value = df.sort_index(ascending=False, inplace=True)
assert return_value is None
expected = frame[::-1]
tm.assert_frame_equal(df, expected)

# axis=1
unordered = frame.loc[:, ["D", "B", "C", "A"]]
df = unordered.copy()
return_value = df.sort_index(axis=1, inplace=True)
assert return_value is None
expected = frame
tm.assert_frame_equal(df, expected)

df = unordered.copy()
return_value = df.sort_index(axis=1, ascending=False, inplace=True)
assert return_value is None
expected = frame.iloc[:, ::-1]
tm.assert_frame_equal(df, expected)
