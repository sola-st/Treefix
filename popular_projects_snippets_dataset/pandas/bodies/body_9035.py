# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
dense = arr.to_dense()
for i, value in enumerate(arr):
    tm.assert_almost_equal(value, dense[i])
    tm.assert_almost_equal(arr[-i], dense[-i])
