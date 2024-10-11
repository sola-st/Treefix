# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
frame = DataFrame(
    np.random.randn(4, 4), index=[1, 2, 3, 4], columns=["A", "B", "C", "D"]
)

sorted_df = frame.copy()
return_value = sorted_df.sort_values(by="A", inplace=True)
assert return_value is None
expected = frame.sort_values(by="A")
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.copy()
return_value = sorted_df.sort_values(by=1, axis=1, inplace=True)
assert return_value is None
expected = frame.sort_values(by=1, axis=1)
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.copy()
return_value = sorted_df.sort_values(by="A", ascending=False, inplace=True)
assert return_value is None
expected = frame.sort_values(by="A", ascending=False)
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.copy()
return_value = sorted_df.sort_values(
    by=["A", "B"], ascending=False, inplace=True
)
assert return_value is None
expected = frame.sort_values(by=["A", "B"], ascending=False)
tm.assert_frame_equal(sorted_df, expected)
