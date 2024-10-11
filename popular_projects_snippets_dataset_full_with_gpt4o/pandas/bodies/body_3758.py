# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
#  GH-46001
foo_index = Index([1, 2, 3], name="foo")
bar_index = Index([1, 2], name="bar")

series = Series(
    [1, 2, 3, 4], index=Index([1, 2, 3, 4], name="bar"), name="foo_series"
)
df = DataFrame(
    {"col": np.arange(6)},
    index=pd.MultiIndex.from_product([foo_index, bar_index]),
)

expected_r = Series([1, 2] * 3, index=df.index, name="foo_series")
result_l, result_r = df.align(series, axis=0)

tm.assert_frame_equal(result_l, df)
tm.assert_series_equal(result_r, expected_r)
