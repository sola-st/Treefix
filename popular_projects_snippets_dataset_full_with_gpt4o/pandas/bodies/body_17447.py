# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
dt = expecteds[offset_types.__name__]
offset_s = _create_offset(offset_types)
assert offset_s.is_on_offset(dt)

# when normalize=True, is_on_offset checks time is 00:00:00
if issubclass(offset_types, Tick):
    # normalize=True disallowed for Tick subclasses GH#21427
    exit()
offset_n = _create_offset(offset_types, normalize=True)
assert not offset_n.is_on_offset(dt)

if offset_types in (BusinessHour, CustomBusinessHour):
    # In default BusinessHour (9:00-17:00), normalized time
    # cannot be in business hour range
    exit()
date = datetime(dt.year, dt.month, dt.day)
assert offset_n.is_on_offset(date)
