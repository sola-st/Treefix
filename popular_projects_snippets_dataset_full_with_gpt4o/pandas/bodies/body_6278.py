# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
# https://github.com/pandas-dev/pandas/issues/32395
ser = pd.Series(data, name="data")
result = pd.Series(index=ser.index, dtype=object, name="data")

# because result has object dtype, the attempt to do setting inplace
#  is successful, and object dtype is retained
key = full_indexer(ser)
result.loc[key] = ser

expected = pd.Series(
    data.astype(object), index=ser.index, name="data", dtype=object
)
self.assert_series_equal(result, expected)
