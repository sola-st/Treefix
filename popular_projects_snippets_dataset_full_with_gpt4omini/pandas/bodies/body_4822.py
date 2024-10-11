# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
mixed = Series(["a_b_c", np.nan, "d_e_f", True, datetime.today(), None, 1, 2.0])
result = getattr(mixed.str, method)("_", expand=expand)
exp = Series(
    [
        ["a", "b", "c"],
        np.nan,
        ["d", "e", "f"],
        np.nan,
        np.nan,
        np.nan,
        np.nan,
        np.nan,
    ]
)
assert isinstance(result, Series)
tm.assert_almost_equal(result, exp)
