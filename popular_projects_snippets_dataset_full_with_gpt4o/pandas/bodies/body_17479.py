# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH#33757 off.name with n != 1 should not raise AttributeError
obj = month_classes(1)
obj2 = month_classes(2)
assert obj2.name == obj.name
