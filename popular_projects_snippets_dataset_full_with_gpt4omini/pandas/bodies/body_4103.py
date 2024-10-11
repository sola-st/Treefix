# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#35450
df = DataFrame(
    data=[
        [1, np.nan, np.nan, True],
        [np.nan, 2, np.nan, True],
        [np.nan, np.nan, np.nan, True],
        [np.nan, np.nan, "5", np.nan],
    ]
)
result = getattr(df, bool_agg_func)(axis=axis, skipna=skipna)
expected = Series([True, True, True, True])
tm.assert_series_equal(result, expected)
