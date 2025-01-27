# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-12300
assert get_nat("NaT").isoformat() == "NaT"
assert get_nat("NaT").isoformat(timespec="nanoseconds") == "NaT"
