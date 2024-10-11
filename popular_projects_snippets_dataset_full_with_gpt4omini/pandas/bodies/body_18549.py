# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
# GH 25851
# ensure that subclassed datetime works with
# localize_pydatetime
result = conversion.localize_pydatetime(dt, UTC)
assert result == expected
