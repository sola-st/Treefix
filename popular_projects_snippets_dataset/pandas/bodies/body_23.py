# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH21224
msg = r"[Cc]ould not convert|can't multiply sequence by non-int of type"
with pytest.raises(expected, match=msg):
    # e.g. Series('a b'.split()).cumprod() will raise
    series.agg(func)
