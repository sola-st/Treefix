# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#38723 these may not be the desired long-term behavior (GH#34479)
#  but in the interim should be internally consistent
dta = date_range("1995-01-02", periods=3)._data
ser = Series(dta)
df = DataFrame(ser)

assert dta.all()
assert dta.any()

assert ser.all()
assert ser.any()

assert df.any().all()
assert df.all().all()

dta = dta.tz_localize("UTC")
ser = Series(dta)
df = DataFrame(ser)

assert dta.all()
assert dta.any()

assert ser.all()
assert ser.any()

assert df.any().all()
assert df.all().all()

tda = dta - dta[0]
ser = Series(tda)
df = DataFrame(ser)

assert tda.any()
assert not tda.all()

assert ser.any()
assert not ser.all()

assert df.any().all()
assert not df.all().any()
