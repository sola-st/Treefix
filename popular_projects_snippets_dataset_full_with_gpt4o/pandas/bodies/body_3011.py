# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
df = DataFrame(np.array([["hello", "goodbye"], ["hello", "Hello"]]))

result = df.sort_values(1)
expected = df[::-1]
tm.assert_frame_equal(result, expected)

result = df.sort_values([0, 1], key=lambda col: col.str.lower())
tm.assert_frame_equal(result, df)

result = df.sort_values(
    [0, 1], key=lambda col: col.str.lower(), ascending=False
)
expected = df.sort_values(1, key=lambda col: col.str.lower(), ascending=False)
tm.assert_frame_equal(result, expected)
