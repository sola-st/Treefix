# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH#38708
series = Series(data)
result = repr(series)
assert result == expected
