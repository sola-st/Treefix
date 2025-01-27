# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
# GH#21404 changed __eq__ to return False when `normalize` does not match
offset = _offset()
offset2 = _offset(normalize=True)
assert offset != offset2
