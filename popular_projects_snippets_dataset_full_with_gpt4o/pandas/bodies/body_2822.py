# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/12392
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
expected = DataFrame(
    {"A": [1, 2, np.nan], "B": [4, 5, np.nan]}, index=[0, 1, 3]
)
result = df.reindex([0, 1, 3])
tm.assert_frame_equal(result, expected)

result = df.reindex([0, 1, 3], axis=0)
tm.assert_frame_equal(result, expected)

result = df.reindex([0, 1, 3], axis="index")
tm.assert_frame_equal(result, expected)
