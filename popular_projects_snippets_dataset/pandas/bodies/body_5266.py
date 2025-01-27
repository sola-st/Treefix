# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("nat", freq="W-SUN")
assert p is NaT

p = Period(iNaT, freq="D")
assert p is NaT

p = Period(iNaT, freq="3D")
assert p is NaT

p = Period(iNaT, freq="1D1H")
assert p is NaT

p = Period("NaT")
assert p is NaT

p = Period(iNaT)
assert p is NaT
