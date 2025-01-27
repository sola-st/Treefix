# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py

# inplace ops / ops alignment
# GH 8511

columns = list("abcdefg")
X_orig = DataFrame(
    np.arange(10 * len(columns)).reshape(-1, len(columns)),
    columns=columns,
    index=range(10),
)
Z = 100 * X_orig.iloc[:, 1:-1].copy()
block1 = list("bedcf")
subs = list("bcdef")

# add
X = X_orig.copy()
result1 = (X[block1] + Z).reindex(columns=subs)

X[block1] += Z
result2 = X.reindex(columns=subs)

X = X_orig.copy()
result3 = (X[block1] + Z[block1]).reindex(columns=subs)

X[block1] += Z[block1]
result4 = X.reindex(columns=subs)

tm.assert_frame_equal(result1, result2)
tm.assert_frame_equal(result1, result3)
tm.assert_frame_equal(result1, result4)

# sub
X = X_orig.copy()
result1 = (X[block1] - Z).reindex(columns=subs)

X[block1] -= Z
result2 = X.reindex(columns=subs)

X = X_orig.copy()
result3 = (X[block1] - Z[block1]).reindex(columns=subs)

X[block1] -= Z[block1]
result4 = X.reindex(columns=subs)

tm.assert_frame_equal(result1, result2)
tm.assert_frame_equal(result1, result3)
tm.assert_frame_equal(result1, result4)
