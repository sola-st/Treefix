# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
cond = klass(self._cond)

exp = klass([obj[0], fill_val, obj[2], fill_val], dtype=exp_dtype)
self._assert_where_conversion(obj, cond, fill_val, exp, exp_dtype)

values, exp = self._construct_exp(obj, klass, fill_val, exp_dtype)
self._assert_where_conversion(obj, cond, values, exp, exp_dtype)
