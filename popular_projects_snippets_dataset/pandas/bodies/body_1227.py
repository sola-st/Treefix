# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series

obj = klass(pd.date_range("2011-01-01", periods=4, freq="D")._with_freq(None))
assert obj.dtype == "datetime64[ns]"

fv = fill_val
# do the check with each of the available datetime scalars
if exp_dtype == "datetime64[ns]":
    for scalar in [fv, fv.to_pydatetime(), fv.to_datetime64()]:
        self._run_test(obj, scalar, klass, exp_dtype)
else:
    for scalar in [fv, fv.to_pydatetime()]:
        self._run_test(obj, fill_val, klass, exp_dtype)
