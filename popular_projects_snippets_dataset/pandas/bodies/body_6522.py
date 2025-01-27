# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# Ensure that the result of agg is inferred to be decimal dtype
# https://github.com/pandas-dev/pandas/issues/29141

data = make_data()[:5]
df = pd.DataFrame(
    {"id1": [0, 0, 0, 1, 1], "id2": [0, 1, 0, 1, 1], "decimals": DecimalArray(data)}
)

# single key, selected column
expected = pd.Series(to_decimal([data[0], data[3]]))
result = df.groupby("id1")["decimals"].agg(lambda x: x.iloc[0])
tm.assert_series_equal(result, expected, check_names=False)
result = df["decimals"].groupby(df["id1"]).agg(lambda x: x.iloc[0])
tm.assert_series_equal(result, expected, check_names=False)

# multiple keys, selected column
expected = pd.Series(
    to_decimal([data[0], data[1], data[3]]),
    index=pd.MultiIndex.from_tuples([(0, 0), (0, 1), (1, 1)]),
)
result = df.groupby(["id1", "id2"])["decimals"].agg(lambda x: x.iloc[0])
tm.assert_series_equal(result, expected, check_names=False)
result = df["decimals"].groupby([df["id1"], df["id2"]]).agg(lambda x: x.iloc[0])
tm.assert_series_equal(result, expected, check_names=False)

# multiple columns
expected = pd.DataFrame({"id2": [0, 1], "decimals": to_decimal([data[0], data[3]])})
result = df.groupby("id1").agg(lambda x: x.iloc[0])
tm.assert_frame_equal(result, expected, check_names=False)
