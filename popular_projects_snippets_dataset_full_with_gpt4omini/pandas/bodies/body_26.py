# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
df = int_frame_const_col

# > 1 ndim
msg = "too many dims to broadcast|cannot broadcast result"
with pytest.raises(ValueError, match=msg):
    df.apply(func, axis=1, result_type="broadcast")
