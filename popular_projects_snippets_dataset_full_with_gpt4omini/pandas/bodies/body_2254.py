# Extracted from ./data/repos/pandas/pandas/tests/construction/test_extract_array.py
ri = Index(range(5))

expected = ri._values
res = extract_array(ri, extract_numpy=True, extract_range=True)
tm.assert_numpy_array_equal(res, expected)
res = extract_array(ri, extract_numpy=False, extract_range=True)
tm.assert_numpy_array_equal(res, expected)

res = extract_array(ri, extract_numpy=True, extract_range=False)
tm.assert_index_equal(res, ri)
res = extract_array(ri, extract_numpy=False, extract_range=False)
tm.assert_index_equal(res, ri)
