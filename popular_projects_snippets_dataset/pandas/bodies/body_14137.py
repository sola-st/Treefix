# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.9999, 1, 1] * 10)
with option_context("display.max_rows", 10, "display.show_dimensions", False):
    res = repr(s)
exp = (
    "0      1.0000\n1      1.0000\n2      1.0000\n3      "
    "1.0000\n4      1.0000\n        ...  \n125    "
    "1.0000\n126    1.0000\n127    0.9999\n128    "
    "1.0000\n129    1.0000\ndtype: float64"
)
assert res == exp
