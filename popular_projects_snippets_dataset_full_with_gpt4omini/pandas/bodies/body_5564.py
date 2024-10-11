# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 48255
with pytest.raises(ValueError, match="nanosecond must be in 0..999"):
    Timestamp(year=2022, month=1, day=1, nanosecond=nano)
