# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
msg = "percentiles should all be in the interval \\[0, 1\\]"
interpolation, method = interp_method
with pytest.raises(ValueError, match=msg):
    datetime_frame.quantile(invalid, interpolation=interpolation, method=method)
