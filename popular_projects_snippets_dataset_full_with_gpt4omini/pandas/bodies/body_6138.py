# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
df = pd.DataFrame({"A": data[:5], "B": data[:5]})
df.columns = columns
result = df.stack()
expected = df.astype(object).stack()
# we need a second astype(object), in case the constructor inferred
# object -> specialized, as is done for period.
expected = expected.astype(object)

if isinstance(expected, pd.Series):
    assert result.dtype == df.iloc[:, 0].dtype
else:
    assert all(result.dtypes == df.iloc[:, 0].dtype)

result = result.astype(object)
self.assert_equal(result, expected)
