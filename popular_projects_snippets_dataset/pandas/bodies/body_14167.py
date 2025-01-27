# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Issue #30122
# Precision was incorrectly shown

with option_context("display.precision", 0):

    df_value = DataFrame(value)
    assert str(df_value) == expected
