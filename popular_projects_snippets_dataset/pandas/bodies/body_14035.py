# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame([[0.1, 0.5], [0.5, -0.1]])
reset_option("display.chop_threshold")  # default None
assert repr(df) == "     0    1\n0  0.1  0.5\n1  0.5 -0.1"

with option_context("display.chop_threshold", 0.2):
    assert repr(df) == "     0    1\n0  0.0  0.5\n1  0.5  0.0"

with option_context("display.chop_threshold", 0.6):
    assert repr(df) == "     0    1\n0  0.0  0.0\n1  0.0  0.0"

with option_context("display.chop_threshold", None):
    assert repr(df) == "     0    1\n0  0.1  0.5\n1  0.5 -0.1"
