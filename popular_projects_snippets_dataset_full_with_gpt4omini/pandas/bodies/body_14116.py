# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH#40024
df = Series([1000.0, "test"])
with option_context("display.float_format", float_format):
    result = repr(df)

assert result == expected
