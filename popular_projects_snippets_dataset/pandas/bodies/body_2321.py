# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#16979
df = DataFrame(np.arange(2 * 3).reshape(2, 3), columns=list("ABC"))
mask = np.array([[True, False, False], [False, False, True]])

result = df.where(mask)
expected = DataFrame(
    [[0, np.nan, np.nan], [np.nan, np.nan, 5]], columns=list("ABC")
)

tm.assert_frame_equal(result, expected)
