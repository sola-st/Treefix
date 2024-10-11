# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH8258, tests that both rows & columns are aligned to what is
# assigned to. covers both uniform data-type & multi-type cases
def run_tests(df, rhs, right_loc, right_iloc):
    # label, index, slice
    lbl_one, idx_one, slice_one = list("bcd"), [1, 2, 3], slice(1, 4)
    lbl_two, idx_two, slice_two = ["joe", "jolie"], [1, 2], slice(1, 3)

    left = df.copy()
    left.loc[lbl_one, lbl_two] = rhs
    tm.assert_frame_equal(left, right_loc)

    left = df.copy()
    left.iloc[idx_one, idx_two] = rhs
    tm.assert_frame_equal(left, right_iloc)

    left = df.copy()
    left.iloc[slice_one, slice_two] = rhs
    tm.assert_frame_equal(left, right_iloc)

xs = np.arange(20).reshape(5, 4)
cols = ["jim", "joe", "jolie", "joline"]
df = DataFrame(xs, columns=cols, index=list("abcde"), dtype="int64")

# right hand side; permute the indices and multiplpy by -2
rhs = -2 * df.iloc[3:0:-1, 2:0:-1]

# expected `right` result; just multiply by -2
right_iloc = df.copy()
right_iloc["joe"] = [1, 14, 10, 6, 17]
right_iloc["jolie"] = [2, 13, 9, 5, 18]
right_iloc.iloc[1:4, 1:3] *= -2
right_loc = df.copy()
right_loc.iloc[1:4, 1:3] *= -2

# run tests with uniform dtypes
run_tests(df, rhs, right_loc, right_iloc)

# make frames multi-type & re-run tests
for frame in [df, rhs, right_loc, right_iloc]:
    frame["joe"] = frame["joe"].astype("float64")
    frame["jolie"] = frame["jolie"].map(lambda x: f"@{x}")
right_iloc["joe"] = [1.0, "@-28", "@-20", "@-12", 17.0]
right_iloc["jolie"] = ["@2", -26.0, -18.0, -10.0, "@18"]
run_tests(df, rhs, right_loc, right_iloc)
