# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
ser = Series(["a\n\r\tb"], name="a\n\r\td", index=["a\n\r\tf"])
assert "\t" not in repr(ser)
assert "\r" not in repr(ser)
assert "a\n" not in repr(ser)
