# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
stamp = Timestamp("2000-01-05 05:09:15.13")
with pytest.raises(ValueError, match=INVALID_FREQ_ERR_MSG):
    stamp.round("foo")
