# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# to confirm test case covers intended dtypes
typ, vals = item
obj = index_or_series(vals)
if isinstance(obj, Index):
    assert obj.dtype == typ
elif isinstance(obj, Series):
    if typ.startswith("period"):
        assert obj.dtype == "Period[M]"
    else:
        assert obj.dtype == typ
