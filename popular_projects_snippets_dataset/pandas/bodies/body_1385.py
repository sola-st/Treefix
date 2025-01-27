# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#11485
df = DataFrame({"X": [1, 2, 3, 4], "Y": list("aabb")}, index=list("ABCD"))

# return location
res = df.iloc[lambda x: [1, 3]]
tm.assert_frame_equal(res, df.iloc[[1, 3]])

res = df.iloc[lambda x: [1, 3], :]
tm.assert_frame_equal(res, df.iloc[[1, 3], :])

res = df.iloc[lambda x: [1, 3], lambda x: 0]
tm.assert_series_equal(res, df.iloc[[1, 3], 0])

res = df.iloc[lambda x: [1, 3], lambda x: [0]]
tm.assert_frame_equal(res, df.iloc[[1, 3], [0]])

# mixture
res = df.iloc[[1, 3], lambda x: 0]
tm.assert_series_equal(res, df.iloc[[1, 3], 0])

res = df.iloc[[1, 3], lambda x: [0]]
tm.assert_frame_equal(res, df.iloc[[1, 3], [0]])

res = df.iloc[lambda x: [1, 3], 0]
tm.assert_series_equal(res, df.iloc[[1, 3], 0])

res = df.iloc[lambda x: [1, 3], [0]]
tm.assert_frame_equal(res, df.iloc[[1, 3], [0]])
