# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py

# this is chained, but ok
with option_context("chained_assignment", None):
    Y = DataFrame(
        np.random.random((4, 4)),
        index=("a", "b", "c", "d"),
        columns=("e", "f", "g", "h"),
    )
    repr(Y)
    Y["e"] = Y["e"].astype("object")
    Y["g"]["c"] = np.NaN
    repr(Y)
    result = Y.sum()  # noqa
    exp = Y["g"].sum()  # noqa
    if using_copy_on_write:
        assert not pd.isna(Y["g"]["c"])
    else:
        assert pd.isna(Y["g"]["c"])
