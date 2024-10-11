# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22163 ensure DataFrame doesn't cast Timestamp to i8
# GH#9631
tz = tz_naive_fixture

dti = date_range("2016-01-01", periods=3, tz=tz)
if tz is None:
    dti2 = dti.tz_localize("US/Eastern")
else:
    dti2 = dti.tz_localize(None)
dtarr = tm.box_expected(dti, box_with_array)

assert_cannot_add(dtarr, dti.values)
assert_cannot_add(dtarr, dti)
assert_cannot_add(dtarr, dtarr)
assert_cannot_add(dtarr, dti[0])
assert_cannot_add(dtarr, dti[0].to_pydatetime())
assert_cannot_add(dtarr, dti[0].to_datetime64())
assert_cannot_add(dtarr, dti2[0])
assert_cannot_add(dtarr, dti2[0].to_pydatetime())
assert_cannot_add(dtarr, np.datetime64("2011-01-01", "D"))
