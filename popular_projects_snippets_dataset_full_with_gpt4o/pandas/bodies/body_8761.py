# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
assert PeriodDtype in registry.dtypes
result = registry.find("Period[D]")
expected = PeriodDtype("D")
assert result == expected
