# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
# GH 17452
off = _offset(weekmask="Mon Wed Fri")
assert off == off.copy()
