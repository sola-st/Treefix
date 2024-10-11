# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
# GH 46870
df = DataFrame(
    {
        "a": [1, 2, 3],
        "b": pd.Series([True, False, True], dtype="boolean"),
        "c": np.array([True, False, True]),
        "d": pd.Categorical([True, False, True]),
        "e": pd.arrays.SparseArray([True, False, True]),
    }
)
result = df.select_dtypes(include="number")
expected = DataFrame({"a": [1, 2, 3]})
tm.assert_frame_equal(result, expected)
