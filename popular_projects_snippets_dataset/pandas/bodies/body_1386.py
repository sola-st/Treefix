# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#11485
df = DataFrame({"X": [1, 2, 3, 4], "Y": list("aabb")}, index=list("ABCD"))

# return location
res = df.copy()
res.iloc[lambda x: [1, 3]] = 0
exp = df.copy()
exp.iloc[[1, 3]] = 0
tm.assert_frame_equal(res, exp)

res = df.copy()
res.iloc[lambda x: [1, 3], :] = -1
exp = df.copy()
exp.iloc[[1, 3], :] = -1
tm.assert_frame_equal(res, exp)

res = df.copy()
res.iloc[lambda x: [1, 3], lambda x: 0] = 5
exp = df.copy()
exp.iloc[[1, 3], 0] = 5
tm.assert_frame_equal(res, exp)

res = df.copy()
res.iloc[lambda x: [1, 3], lambda x: [0]] = 25
exp = df.copy()
exp.iloc[[1, 3], [0]] = 25
tm.assert_frame_equal(res, exp)

# mixture
res = df.copy()
res.iloc[[1, 3], lambda x: 0] = -3
exp = df.copy()
exp.iloc[[1, 3], 0] = -3
tm.assert_frame_equal(res, exp)

res = df.copy()
res.iloc[[1, 3], lambda x: [0]] = -5
exp = df.copy()
exp.iloc[[1, 3], [0]] = -5
tm.assert_frame_equal(res, exp)

res = df.copy()
res.iloc[lambda x: [1, 3], 0] = 10
exp = df.copy()
exp.iloc[[1, 3], 0] = 10
tm.assert_frame_equal(res, exp)

res = df.copy()
res.iloc[lambda x: [1, 3], [0]] = [-5, -5]
exp = df.copy()
exp.iloc[[1, 3], [0]] = [-5, -5]
tm.assert_frame_equal(res, exp)
