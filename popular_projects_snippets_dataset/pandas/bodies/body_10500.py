# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# GH 9052
# make sure that the aggregates via dict
# are consistent
df = DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "two", "two", "two", "one", "two"],
        "C": np.random.randn(8) + 1.0,
        "D": np.arange(8),
    }
)

grouped = df.groupby(["A", "B"])
c_mean = grouped["C"].mean()
c_sum = grouped["C"].sum()
d_mean = grouped["D"].mean()
d_sum = grouped["D"].sum()

result = grouped["D"].agg(["sum", "mean"])
expected = pd.concat([d_sum, d_mean], axis=1)
expected.columns = ["sum", "mean"]
tm.assert_frame_equal(result, expected, check_like=True)

result = grouped.agg([np.sum, np.mean])
expected = pd.concat([c_sum, c_mean, d_sum, d_mean], axis=1)
expected.columns = MultiIndex.from_product([["C", "D"], ["sum", "mean"]])
tm.assert_frame_equal(result, expected, check_like=True)

result = grouped[["D", "C"]].agg([np.sum, np.mean])
expected = pd.concat([d_sum, d_mean, c_sum, c_mean], axis=1)
expected.columns = MultiIndex.from_product([["D", "C"], ["sum", "mean"]])
tm.assert_frame_equal(result, expected, check_like=True)

result = grouped.agg({"C": "mean", "D": "sum"})
expected = pd.concat([d_sum, c_mean], axis=1)
tm.assert_frame_equal(result, expected, check_like=True)

result = grouped.agg({"C": ["mean", "sum"], "D": ["mean", "sum"]})
expected = pd.concat([c_mean, c_sum, d_mean, d_sum], axis=1)
expected.columns = MultiIndex.from_product([["C", "D"], ["mean", "sum"]])

msg = r"Column\(s\) \['r', 'r2'\] do not exist"
with pytest.raises(KeyError, match=msg):
    grouped[["D", "C"]].agg({"r": np.sum, "r2": np.mean})
