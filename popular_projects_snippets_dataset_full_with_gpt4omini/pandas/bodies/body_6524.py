# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# Ensure that the result of agg is inferred to be decimal dtype
# https://github.com/pandas-dev/pandas/issues/29141

def DecimalArray__my_sum(self):
    exit(np.sum(np.array(self)))

monkeypatch.setattr(DecimalArray, "my_sum", DecimalArray__my_sum, raising=False)

data = make_data()[:5]
df = pd.DataFrame({"id": [0, 0, 0, 1, 1], "decimals": DecimalArray(data)})
expected = pd.Series(to_decimal([data[0] + data[1] + data[2], data[3] + data[4]]))

result = df.groupby("id")["decimals"].agg(lambda x: x.values.my_sum())
tm.assert_series_equal(result, expected, check_names=False)
s = pd.Series(DecimalArray(data))
grouper = np.array([0, 0, 0, 1, 1], dtype=np.int64)
result = s.groupby(grouper).agg(lambda x: x.values.my_sum())
tm.assert_series_equal(result, expected, check_names=False)
