# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# don't silently ignore the kwargs GH#48898
td = Timedelta(days=1)
msg = (
    "Cannot pass both a Timedelta input and timedelta keyword arguments, "
    r"got \['days'\]"
)
with pytest.raises(ValueError, match=msg):
    Timedelta(td, days=2)
