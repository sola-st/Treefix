# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH#16793
df = DataFrame({"x": Categorical(np.repeat([1, 2, 3, 4], 5), ordered=True)})
expected = df.copy()
sorted_df = df.sort_values("x", kind="mergesort")
tm.assert_frame_equal(sorted_df, expected)
