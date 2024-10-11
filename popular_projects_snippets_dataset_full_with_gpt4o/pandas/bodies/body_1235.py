# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
"""test coercion triggered by fillna"""
target = original.copy()
res = target.fillna(value)
tm.assert_equal(res, expected)
assert res.dtype == expected_dtype
