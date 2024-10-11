# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 25960
msg = """
One or more strings in the dta file could not be decoded using utf-8, and
so the fallback encoding of latin-1 is being used.  This can happen when a file
has been incorrectly encoded by Stata or some other software. You should verify
the string values returned are correct."""
with tm.assert_produces_warning(UnicodeWarning) as w:
    encoded = read_stata(
        datapath("io", "data", "stata", "stata1_encoding_118.dta")
    )
    assert len(w) == 151
    assert w[0].message.args[0] == msg

expected = DataFrame([["Düsseldorf"]] * 151, columns=["kreis1849"])
tm.assert_frame_equal(encoded, expected)
