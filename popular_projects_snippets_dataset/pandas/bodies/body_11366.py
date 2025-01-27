# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting multiple columns with a column indexer on a viewing subset
# -> subset.loc[:, [col1, col2]] = value
df = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3], "c": [4, 5, 6]})
df_orig = df.copy()
subset = df[1:3]

if using_copy_on_write:
    subset.loc[:, indexer] = 0
else:
    with pd.option_context("chained_assignment", "warn"):
        # As of 2.0, this setitem attempts (successfully) to set values
        #  inplace, so the assignment is not chained.
        subset.loc[:, indexer] = 0

subset._mgr._verify_integrity()
expected = DataFrame({"a": [0, 0], "b": [0.0, 0.0], "c": [5, 6]}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    # pre-2.0, in the mixed case with BlockManager, only column "a"
    #  would be mutated in the parent frame. this changed with the
    #  enforcement of GH#45333
    df_orig.loc[1:2, ["a", "b"]] = 0
    tm.assert_frame_equal(df, df_orig)
