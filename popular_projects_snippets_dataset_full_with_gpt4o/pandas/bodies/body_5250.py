# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#44507
td = NaT.to_numpy("m8[ns]")

msg = "Value must be Period, string, integer, or datetime"
with pytest.raises(ValueError, match=msg):
    Period(td)

with pytest.raises(ValueError, match=msg):
    Period(td, freq="D")
