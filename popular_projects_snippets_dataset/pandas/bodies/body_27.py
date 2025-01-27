# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# cannot both transform and agg
msg = "cannot combine transform and aggregation operations"
with pytest.raises(ValueError, match=msg):
    with np.errstate(all="ignore"):
        float_frame.agg(["max", "sqrt"], axis=axis)
