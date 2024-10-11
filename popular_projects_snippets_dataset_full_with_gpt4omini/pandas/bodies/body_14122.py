# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series(["\u03c3"] * 10)
repr(s)

a = Series(["\u05d0"] * 1000)
a.name = "title1"
repr(a)
