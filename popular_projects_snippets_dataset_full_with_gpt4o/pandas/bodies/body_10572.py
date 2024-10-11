# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
gb = df.groupby(level=0)
if reduction_func in ("idxmax", "idxmin"):
    error = TypeError
    msg = "reduction operation '.*' not allowed for this dtype"
else:
    error = ValueError
    msg = f"Operation {reduction_func} does not support axis=1"
with pytest.raises(error, match=msg):
    gb.agg(reduction_func, axis=1)
