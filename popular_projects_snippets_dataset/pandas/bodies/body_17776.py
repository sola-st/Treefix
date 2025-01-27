# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
with pytest.raises(ValueError, match=INVALID_FREQ_ERR_MSG):
    offset_func(freq)
