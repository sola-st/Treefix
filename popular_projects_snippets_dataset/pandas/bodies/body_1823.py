# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 16231
cols = pd.MultiIndex.from_tuples([("A", "a", "", "one"), ("B", "b", "i", "two")])
ind = date_range(start="2017-01-01", freq="15Min", periods=8)
df = DataFrame(np.array([0] * 16).reshape(8, 2), index=ind, columns=cols)
agg_dict = {col: (np.sum if col[3] == "one" else np.mean) for col in df.columns}
result = df.resample("H").apply(lambda x: agg_dict[x.name](x))
expected = DataFrame(
    2 * [[0, 0.0]],
    index=date_range(start="2017-01-01", freq="1H", periods=2),
    columns=pd.MultiIndex.from_tuples(
        [("A", "a", "", "one"), ("B", "b", "i", "two")]
    ),
)
tm.assert_frame_equal(result, expected)
