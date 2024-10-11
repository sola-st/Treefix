# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 8844
full_multiindex = MultiIndex.from_tuples(
    [("B", "x"), ("B", "z"), ("A", "y"), ("C", "x"), ("C", "u")],
    names=["Upper", "Lower"],
)
multiindex = full_multiindex[multiindex_columns]
df = DataFrame(
    np.arange(3 * len(multiindex)).reshape(3, len(multiindex)),
    columns=multiindex,
)
result = df.stack(level=level, dropna=False)

if isinstance(level, int):
    # Stacking a single level should not make any all-NaN rows,
    # so df.stack(level=level, dropna=False) should be the same
    # as df.stack(level=level, dropna=True).
    expected = df.stack(level=level, dropna=True)
    if isinstance(expected, Series):
        tm.assert_series_equal(result, expected)
    else:
        tm.assert_frame_equal(result, expected)

df.columns = MultiIndex.from_tuples(
    df.columns.to_numpy(), names=df.columns.names
)
expected = df.stack(level=level, dropna=False)
if isinstance(expected, Series):
    tm.assert_series_equal(result, expected)
else:
    tm.assert_frame_equal(result, expected)
