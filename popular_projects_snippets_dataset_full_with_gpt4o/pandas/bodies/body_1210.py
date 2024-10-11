# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
"""test coercion triggered by insert"""
target = original.copy()
res = target.insert(1, value)
tm.assert_index_equal(res, expected)
assert res.dtype == expected_dtype
