# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
assert repr(offset1) == "<BusinessHour: BH=09:00-17:00>"
assert repr(offset2) == "<3 * BusinessHours: BH=09:00-17:00>"
assert repr(offset3) == "<-1 * BusinessHour: BH=09:00-17:00>"
assert repr(offset4) == "<-4 * BusinessHours: BH=09:00-17:00>"

assert repr(offset5) == "<BusinessHour: BH=11:00-14:30>"
assert repr(offset6) == "<BusinessHour: BH=20:00-05:00>"
assert repr(offset7) == "<-2 * BusinessHours: BH=21:30-06:30>"
assert repr(offset8) == "<BusinessHour: BH=09:00-12:00,13:00-17:00>"
assert repr(offset9) == "<3 * BusinessHours: BH=09:00-13:00,22:00-03:00>"
assert repr(offset10) == "<-1 * BusinessHour: BH=13:00-17:00,23:00-02:00>"
