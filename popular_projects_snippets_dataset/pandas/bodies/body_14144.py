# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# gh-7117
s = Series(range(5))

assert "Length" not in repr(s)

with option_context("display.max_rows", 4):
    assert "Length" in repr(s)

with option_context("display.show_dimensions", True):
    assert "Length" in repr(s)

with option_context("display.max_rows", 4, "display.show_dimensions", False):
    assert "Length" not in repr(s)
