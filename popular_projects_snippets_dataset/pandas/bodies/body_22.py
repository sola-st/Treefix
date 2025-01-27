# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 21224
msg = "can't multiply sequence by non-int of type 'str'"
with pytest.raises(expected, match=msg):
    df.agg(func, axis=axis)
