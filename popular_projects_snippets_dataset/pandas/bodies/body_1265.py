# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# this is chained assignment, but will 'work'
with option_context("chained_assignment", None):

    # #3970
    df = DataFrame({"aa": np.arange(5), "bb": [2.2] * 5})

    # Creates a second float block
    df["cc"] = 0.0

    # caches a reference to the 'bb' series
    df["bb"]

    # repr machinery triggers consolidation
    repr(df)

    # Assignment to wrong series
    df["bb"].iloc[0] = 0.17
    df._clear_item_cache()
    if not using_copy_on_write:
        tm.assert_almost_equal(df["bb"][0], 0.17)
    else:
        # with ArrayManager, parent is not mutated with chained assignment
        tm.assert_almost_equal(df["bb"][0], 2.2)
