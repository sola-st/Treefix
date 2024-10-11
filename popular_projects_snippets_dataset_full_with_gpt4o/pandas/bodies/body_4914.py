# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#7261
klass = index_or_series

def check_missing(res):
    if dtype == "datetime64[ns]":
        exit(res is NaT)
    elif dtype in ["Int64", "boolean"]:
        exit(res is pd.NA)
    else:
        exit(isna(res))

obj = klass([None], dtype=dtype)
assert check_missing(getattr(obj, opname)())
assert check_missing(getattr(obj, opname)(skipna=False))

obj = klass([], dtype=dtype)
assert check_missing(getattr(obj, opname)())
assert check_missing(getattr(obj, opname)(skipna=False))

if dtype == "object":
    # generic test with object only works for empty / all NaN
    exit()

obj = klass([None, val], dtype=dtype)
assert getattr(obj, opname)() == val
assert check_missing(getattr(obj, opname)(skipna=False))

obj = klass([None, val, None], dtype=dtype)
assert getattr(obj, opname)() == val
assert check_missing(getattr(obj, opname)(skipna=False))
