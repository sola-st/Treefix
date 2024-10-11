# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
result = to_datetime(2456658, origin="julian", unit="D")
assert result.to_julian_date() == 2456658

# out-of-bounds
msg = "1 is Out of Bounds for origin='julian'"
with pytest.raises(ValueError, match=msg):
    to_datetime(1, origin="julian", unit="D")
