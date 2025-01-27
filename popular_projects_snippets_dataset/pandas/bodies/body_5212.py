# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert td // np.nan is NaT

res = td // 2
assert res.value == td.value // 2
assert res._creso == td._creso

res = td // 2.0
assert res.value == td.value // 2
assert res._creso == td._creso

assert td // np.array(np.nan) is NaT

res = td // np.array(2)
assert res.value == td.value // 2
assert res._creso == td._creso

res = td // np.array(2.0)
assert res.value == td.value // 2
assert res._creso == td._creso
