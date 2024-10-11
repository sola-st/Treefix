# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
# issue 18478
result = converter.TimeFormatter(None)(time)
assert result == format_expected
