# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py

pi = pd.period_range("2016-01-01", periods=4, freq="D").insert(1, pd.NaT)
assert isinstance(pi.dtype, pd.PeriodDtype)
obj = index_or_series(pi)

exp = index_or_series([pi[0], fill_val, pi[2], pi[3], pi[4]], dtype=object)

fill_dtype = object
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
