# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 30880
# ohlc expands dimensions, so different test to the above is required.
df = DataFrame(
    np.random.randn(1000, 3),
    index=pd.date_range("1/1/2012", freq="S", periods=1000, name="dti"),
    columns=Index(["A", "B", "C"], name="alpha"),
)
result = df.resample("3T").agg(
    {"A": ["ohlc", partial(np.quantile, q=0.9999), partial(np.quantile, q=0.1111)]}
)
expected_index = pd.date_range("1/1/2012", freq="3T", periods=6, name="dti")
expected_columns = MultiIndex.from_tuples(
    [
        ("A", "ohlc", "open"),
        ("A", "ohlc", "high"),
        ("A", "ohlc", "low"),
        ("A", "ohlc", "close"),
        ("A", "quantile", "A"),
        ("A", "quantile", "A"),
    ],
    names=["alpha", None, None],
)
non_ohlc_expected_values = np.array(
    [df.resample("3T").A.quantile(q=q).values for q in [0.9999, 0.1111]]
).T
expected_values = np.hstack([df.resample("3T").A.ohlc(), non_ohlc_expected_values])
expected = DataFrame(
    expected_values, columns=expected_columns, index=expected_index
)
tm.assert_frame_equal(result, expected)
