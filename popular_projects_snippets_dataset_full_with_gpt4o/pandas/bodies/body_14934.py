# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
r1 = dtc.convert("2000-01-01 12:22", None, None)
r2 = dtc.convert("2000-01-01 12:22", None, None)
assert r1 == r2, "DatetimeConverter.convert should accept unicode"
