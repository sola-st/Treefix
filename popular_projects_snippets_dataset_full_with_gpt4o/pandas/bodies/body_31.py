# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 35964
op = op_wrapper(all_reductions)

obj = DataFrame({"A": [1, 2, 3]})
obj = tm.get_obj(obj, frame_or_series)

msg = "Function did not transform"
with pytest.raises(ValueError, match=msg):
    obj.transform(op)
