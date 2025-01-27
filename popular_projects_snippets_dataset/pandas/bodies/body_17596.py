# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
weekmask_saudi = "Sat Sun Mon Tue Wed"  # Thu-Fri Weekend
weekmask_uae = "1111001"  # Fri-Sat Weekend
weekmask_egypt = [1, 1, 1, 1, 0, 0, 1]  # Fri-Sat Weekend
bday_saudi = CDay(weekmask=weekmask_saudi)
bday_uae = CDay(weekmask=weekmask_uae)
bday_egypt = CDay(weekmask=weekmask_egypt)
dt = datetime(2013, 5, 1)
xp_saudi = datetime(2013, 5, 4)
xp_uae = datetime(2013, 5, 2)
xp_egypt = datetime(2013, 5, 2)
assert xp_saudi == dt + bday_saudi
assert xp_uae == dt + bday_uae
assert xp_egypt == dt + bday_egypt
xp2 = datetime(2013, 5, 5)
assert xp2 == dt + 2 * bday_saudi
assert xp2 == dt + 2 * bday_uae
assert xp2 == dt + 2 * bday_egypt
