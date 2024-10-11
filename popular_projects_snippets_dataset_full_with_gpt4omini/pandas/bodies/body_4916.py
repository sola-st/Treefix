# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
klass = index_or_series
arg_op = "arg" + opname if klass is Index else "idx" + opname

obj = klass([], dtype=dtype)

assert getattr(obj, opname)() is NaT
assert getattr(obj, opname)(skipna=False) is NaT

with pytest.raises(ValueError, match="empty sequence"):
    getattr(obj, arg_op)()
with pytest.raises(ValueError, match="empty sequence"):
    getattr(obj, arg_op)(skipna=False)
