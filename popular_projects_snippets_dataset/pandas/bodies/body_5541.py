# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 8910
msg = f"Unknown datetime string format, unable to parse: 2014-11-02 01:00{z}"
with pytest.raises(ValueError, match=msg):
    Timestamp(f"2014-11-02 01:00{z}")
