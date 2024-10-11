# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
# https://github.com/pandas-dev/pandas/issues/32395
df = expected = pd.DataFrame({"data": pd.Series(data)})
result = pd.DataFrame(index=df.index)

# because result has object dtype, the attempt to do setting inplace
#  is successful, and object dtype is retained
key = full_indexer(df)
result.loc[key, "data"] = df["data"]

# base class method has expected = df; PandasArray behaves oddly because
#  we patch _typ for these tests.
if data.dtype.numpy_dtype != object:
    if not isinstance(key, slice) or key != slice(None):
        expected = pd.DataFrame({"data": data.to_numpy()})
self.assert_frame_equal(result, expected)
