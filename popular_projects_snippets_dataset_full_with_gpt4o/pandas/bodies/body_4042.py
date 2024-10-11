# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
df = pd.DataFrame(
    {
        "a": pd.array([1, -2, 3, pd.NA], dtype="Int64"),
        "b": pd.array([4.0, -5.0, 6.0, pd.NA], dtype="Float32"),
        "c": pd.array([True, False, False, pd.NA], dtype="boolean"),
        # include numpy bool to make sure bool-vs-boolean behavior
        #  is consistent in non-NA locations
        "d": np.array([True, False, False, True]),
    }
)

result = +df
res_ufunc = np.positive(df)
expected = df
# TODO: assert that we have copies?
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(res_ufunc, expected)

result = -df
res_ufunc = np.negative(df)
expected = pd.DataFrame(
    {
        "a": pd.array([-1, 2, -3, pd.NA], dtype="Int64"),
        "b": pd.array([-4.0, 5.0, -6.0, pd.NA], dtype="Float32"),
        "c": pd.array([False, True, True, pd.NA], dtype="boolean"),
        "d": np.array([False, True, True, False]),
    }
)
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(res_ufunc, expected)

result = abs(df)
res_ufunc = np.abs(df)
expected = pd.DataFrame(
    {
        "a": pd.array([1, 2, 3, pd.NA], dtype="Int64"),
        "b": pd.array([4.0, 5.0, 6.0, pd.NA], dtype="Float32"),
        "c": pd.array([True, False, False, pd.NA], dtype="boolean"),
        "d": np.array([True, False, False, True]),
    }
)
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(res_ufunc, expected)
