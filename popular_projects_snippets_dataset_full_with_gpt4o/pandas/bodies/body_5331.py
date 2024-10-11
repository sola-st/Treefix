# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# GH#19834
per1 = Period("0001-01-01", "D") + 6
per2 = Period("0001-01-01", "D") - 6
week1 = per1.asfreq("W")
week2 = per2.asfreq("W")
assert week1 != week2
assert week1.asfreq("D", "E") >= per1
assert week2.asfreq("D", "S") <= per2
