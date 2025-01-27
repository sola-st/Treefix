# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
tick = offsets.Nano()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_ns.value

tick = offsets.Micro()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_us.value

tick = offsets.Milli()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_ms.value

tick = offsets.Second()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value

# everything above Second gets cast to the closest supported reso: second
tick = offsets.Minute()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value

tick = offsets.Hour()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value

tick = offsets.Day()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
