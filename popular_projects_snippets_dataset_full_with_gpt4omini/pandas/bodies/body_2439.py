# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py

df = DataFrame(np.random.randn(10, 4), index=range(0, 20, 2))
original = df.copy()

# verify slice is view
# setting it makes it raise/warn
subset = df.iloc[slice(4, 8)]

assert np.shares_memory(df[2], subset[2])

exp_col = original[2].copy()
subset.loc[:, 2] = 0.0
if not using_copy_on_write:
    subset.loc[:, 2] = 0.0
    exp_col._values[4:8] = 0.0

    # With the enforcement of GH#45333 in 2.0, this remains a view
    assert np.shares_memory(df[2], subset[2])
tm.assert_series_equal(df[2], exp_col)
