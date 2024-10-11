# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 10451
with option_context("display.precision", 4):
    # need both a number > 1e6 and something that normally formats to
    # having length > display.precision + 6
    df = DataFrame({"x": [12345.6789]})
    assert str(df) == "            x\n0  12345.6789"
    df = DataFrame({"x": [2e6]})
    assert str(df) == "           x\n0  2000000.0"
    df = DataFrame({"x": [12345.6789, 2e6]})
    assert str(df) == "            x\n0  1.2346e+04\n1  2.0000e+06"
