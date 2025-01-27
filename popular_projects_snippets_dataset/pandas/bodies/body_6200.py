# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
# ... but specifying dtype will override idempotency
result = pd.array(data, dtype=np.dtype(object))
expected = pd.arrays.PandasArray(np.asarray(data, dtype=object))
self.assert_equal(result, expected)
