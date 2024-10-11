# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
"""test coercion triggered by where"""
target = original.copy()
res = target.where(cond, values)
tm.assert_equal(res, expected)
assert res.dtype == expected_dtype
