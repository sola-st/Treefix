# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# increasing -> sort doesn't matter
ri = pd.RangeIndex.from_range(range(10))
expected = np.arange(10, dtype=np.intp), ri

result = algos.factorize(ri, sort=sort)
tm.assert_numpy_array_equal(result[0], expected[0])
tm.assert_index_equal(result[1], expected[1], exact=True)

result = ri.factorize(sort=sort)
tm.assert_numpy_array_equal(result[0], expected[0])
tm.assert_index_equal(result[1], expected[1], exact=True)
