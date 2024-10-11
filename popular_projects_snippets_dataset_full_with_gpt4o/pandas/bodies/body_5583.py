# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# decreasing -> sort matters
ri = pd.RangeIndex.from_range(range(10))
expected = np.arange(10, dtype=np.intp), ri

ri2 = ri[::-1]
expected = expected[0], ri2
if sort:
    expected = expected[0][::-1], expected[1][::-1]

result = algos.factorize(ri2, sort=sort)
tm.assert_numpy_array_equal(result[0], expected[0])
tm.assert_index_equal(result[1], expected[1], exact=True)

result = ri2.factorize(sort=sort)
tm.assert_numpy_array_equal(result[0], expected[0])
tm.assert_index_equal(result[1], expected[1], exact=True)
