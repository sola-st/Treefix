# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 30880
df = DataFrame(
    np.random.randn(1000, 3),
    index=pd.date_range("1/1/2012", freq="S", periods=1000),
    columns=["A", "B", "C"],
)
result = df.resample("3T").agg(
    {"A": [partial(np.quantile, q=0.9999), partial(np.quantile, q=0.1111)]}
)
expected_index = pd.date_range("1/1/2012", freq="3T", periods=6)
expected_columns = MultiIndex.from_tuples([("A", "quantile"), ("A", "quantile")])
expected_values = np.array(
    [df.resample("3T").A.quantile(q=q).values for q in [0.9999, 0.1111]]
).T
expected = DataFrame(
    expected_values, columns=expected_columns, index=expected_index
)
tm.assert_frame_equal(result, expected)
