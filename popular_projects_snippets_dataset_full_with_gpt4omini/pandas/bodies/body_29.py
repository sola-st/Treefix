# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 35964
# cannot both transform and agg
msg = "Function did not transform"
with pytest.raises(ValueError, match=msg):
    float_frame.transform(func, axis=axis)
