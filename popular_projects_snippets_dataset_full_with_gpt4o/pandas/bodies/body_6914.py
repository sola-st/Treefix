# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_formats.py
# Enable Unicode option -----------------------------------------
with cf.option_context("display.unicode.east_asian_width", True):
    result = repr(index)
    assert result == expected
