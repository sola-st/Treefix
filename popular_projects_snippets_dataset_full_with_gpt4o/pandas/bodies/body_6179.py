# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# https://github.com/pandas-dev/pandas/issues/23066
data = pd.Series(data)
if as_frame:
    data = data.to_frame()
a = pd.util.hash_pandas_object(data)
b = pd.util.hash_pandas_object(data)
self.assert_equal(a, b)
