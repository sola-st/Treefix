# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# allowed result_type
df = int_frame_const_col

msg = (
    "invalid value for result_type, must be one of "
    "{None, 'reduce', 'broadcast', 'expand'}"
)
with pytest.raises(ValueError, match=msg):
    df.apply(lambda x: [1, 2, 3], axis=1, result_type=result_type)
