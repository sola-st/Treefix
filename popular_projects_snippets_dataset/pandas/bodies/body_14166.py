# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Issue #20359: trimming zeros while there is no decimal point

# Happens when display precision is set to zero
with option_context("display.precision", 0):
    s = Series([840.0, 4200.0])
    expected_output = "0     840\n1    4200\ndtype: float64"
    assert str(s) == expected_output
