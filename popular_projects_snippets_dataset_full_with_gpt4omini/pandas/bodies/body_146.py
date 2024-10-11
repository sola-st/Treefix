# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
no_cols = DataFrame(index=["a", "b", "c"])
result = no_cols.apply(lambda x: x.mean(), result_type="broadcast")
assert isinstance(result, DataFrame)
