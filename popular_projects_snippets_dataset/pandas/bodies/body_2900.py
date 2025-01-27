# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# gh-36562

mi1 = MultiIndex.from_arrays(
    [["b", "b", "c", "a", "b", np.nan], [1, 2, 3, 4, 5, 6]], names=["a", "b"]
)
df = DataFrame({"c": [1, 1, 1, 1, 1, 1]}, index=mi1)
mi2 = MultiIndex.from_arrays(
    [["a", "b", "c", "a", "b", "d"], [1, 1, 1, 1, 1, 1]], names=["a", "b"]
)
s = Series([1, 2, 3, 4, 5, 6], index=mi2)
res = df.combine_first(DataFrame({"d": s}))
mi_expected = MultiIndex.from_arrays(
    [
        ["a", "a", "a", "b", "b", "b", "b", "c", "c", "d", np.nan],
        [1, 1, 4, 1, 1, 2, 5, 1, 3, 1, 6],
    ],
    names=["a", "b"],
)
expected = DataFrame(
    {
        "c": [np.nan, np.nan, 1, 1, 1, 1, 1, np.nan, 1, np.nan, 1],
        "d": [1.0, 4.0, np.nan, 2.0, 5.0, np.nan, np.nan, 3.0, np.nan, 6.0, np.nan],
    },
    index=mi_expected,
)
tm.assert_frame_equal(res, expected)
