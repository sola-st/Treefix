# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
df = DataFrame(np.array([0, 5, np.nan, 3, 2, np.nan]))

result = df.sort_values(0)
expected = df.iloc[[0, 4, 3, 1, 2, 5]]
tm.assert_frame_equal(result, expected)

result = df.sort_values(0, key=lambda x: x + 5)
expected = df.iloc[[0, 4, 3, 1, 2, 5]]
tm.assert_frame_equal(result, expected)

result = df.sort_values(0, key=lambda x: -x, ascending=False)
expected = df.iloc[[0, 4, 3, 1, 2, 5]]
tm.assert_frame_equal(result, expected)
