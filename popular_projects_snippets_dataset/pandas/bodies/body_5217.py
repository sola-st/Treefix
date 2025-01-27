# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# when accessed on the class (as opposed to an instance), we default
#  to nanoseconds
assert Timedelta.min == Timedelta(NaT.value + 1)
assert Timedelta.min._creso == NpyDatetimeUnit.NPY_FR_ns.value

assert Timedelta.max == Timedelta(np.iinfo(np.int64).max)
assert Timedelta.max._creso == NpyDatetimeUnit.NPY_FR_ns.value

assert Timedelta.resolution == Timedelta(1)
assert Timedelta.resolution._creso == NpyDatetimeUnit.NPY_FR_ns.value
