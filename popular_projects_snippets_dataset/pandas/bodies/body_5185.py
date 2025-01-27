# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
msg = f"Invalid ISO 8601 Duration format - {fmt}"
with pytest.raises(ValueError, match=msg):
    Timedelta(fmt)
