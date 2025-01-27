# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 17797
#
# Test that display formats are ignored when determining if a numeric
# column is a date value.
#
# All date types are stored as numbers and format associated with the
# column denotes both the type of the date and the display format.
#
# STATA supports 9 date types which each have distinct units. We test 7
# of the 9 types, ignoring %tC and %tb. %tC is a variant of %tc that
# accounts for leap seconds and %tb relies on STATAs business calendar.
df = read_stata(datapath("io", "data", "stata", "stata13_dates.dta"))
unformatted = df.loc[0, column]
formatted = df.loc[0, column + "_fmt"]
assert unformatted == formatted
