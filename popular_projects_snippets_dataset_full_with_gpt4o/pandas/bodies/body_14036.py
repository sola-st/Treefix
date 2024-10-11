# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 6839: validation case

df = DataFrame([[10, 20, 30, 40], [8e-10, -1e-11, 2e-9, -2e-11]]).T

with option_context("display.chop_threshold", 0):
    assert repr(df) == (
        "      0             1\n"
        "0  10.0  8.000000e-10\n"
        "1  20.0 -1.000000e-11\n"
        "2  30.0  2.000000e-09\n"
        "3  40.0 -2.000000e-11"
    )

with option_context("display.chop_threshold", 1e-8):
    assert repr(df) == (
        "      0             1\n"
        "0  10.0  0.000000e+00\n"
        "1  20.0  0.000000e+00\n"
        "2  30.0  0.000000e+00\n"
        "3  40.0  0.000000e+00"
    )

with option_context("display.chop_threshold", 5e-11):
    assert repr(df) == (
        "      0             1\n"
        "0  10.0  8.000000e-10\n"
        "1  20.0  0.000000e+00\n"
        "2  30.0  2.000000e-09\n"
        "3  40.0  0.000000e+00"
    )
