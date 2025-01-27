# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame(
    [[1, 2], [3, 4], [np.nan, np.nan], [7, 8], [9, 10]],
    columns=["a", "b"],
    index=[100.0, 101.0, np.nan, 102.0, 103.0],
)

result = df.reindex(index=[101.0, 102.0, 103.0])
expected = df.iloc[[1, 3, 4]]
tm.assert_frame_equal(result, expected)

result = df.reindex(index=[103.0])
expected = df.iloc[[4]]
tm.assert_frame_equal(result, expected)

result = df.reindex(index=[101.0])
expected = df.iloc[[1]]
tm.assert_frame_equal(result, expected)
