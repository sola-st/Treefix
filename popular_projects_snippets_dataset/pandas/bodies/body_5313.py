# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#47196
per = Period("2022-06-01", "D")
nat = np.timedelta64("NaT", unit)

assert per + nat is NaT
assert nat + per is NaT
assert per - nat is NaT

with pytest.raises(TypeError, match="unsupported operand"):
    nat - per
