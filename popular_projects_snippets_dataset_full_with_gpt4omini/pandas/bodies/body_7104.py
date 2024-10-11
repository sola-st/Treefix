# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# separately tested
if isinstance(index, CategoricalIndex):
    exit()

result = index.argsort()
expected = np.array(index).argsort()
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
