# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 16646
# Operating on the columns, or transposing and operating on the rows
# should give the same result. There was previously a bug where the
# by_rows operation would work fine, but by_cols would throw a ValueError

df = DataFrame(
    np.random.random([6, 4]),
    columns=MultiIndex.from_product([["A", "B"], [1, 2]]),
)

by_rows = df.T.groupby(axis=0, level=0).apply(
    lambda x: x.droplevel(axis=0, level=0)
)
by_cols = df.groupby(axis=1, level=0).apply(lambda x: x.droplevel(axis=1, level=0))

tm.assert_frame_equal(by_cols, by_rows.T)
tm.assert_frame_equal(by_cols, df)
