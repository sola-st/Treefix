# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
frame = multiindex_dataframe_random_data

sorted_before = frame.sort_index(level=1)

df = frame.copy()
df["foo"] = "bar"
sorted_after = df.sort_index(level=1)
tm.assert_frame_equal(sorted_before, sorted_after.drop(["foo"], axis=1))

dft = frame.T
sorted_before = dft.sort_index(level=1, axis=1)
dft["foo", "three"] = "bar"

sorted_after = dft.sort_index(level=1, axis=1)
tm.assert_frame_equal(
    sorted_before.drop([("foo", "three")], axis=1),
    sorted_after.drop([("foo", "three")], axis=1),
)
