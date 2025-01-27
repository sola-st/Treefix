# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

with option_context("chained_assignment", "raise"):
    # work with the chain
    expected = DataFrame([[-5, 1], [-6, 3]], columns=list("AB"))
    df = DataFrame(
        np.arange(4).reshape(2, 2), columns=list("AB"), dtype="int64"
    )
    df_original = df.copy()
    assert df._is_copy is None

    df["A"][0] = -5
    df["A"][1] = -6
    if using_copy_on_write:
        tm.assert_frame_equal(df, df_original)
    else:
        tm.assert_frame_equal(df, expected)
