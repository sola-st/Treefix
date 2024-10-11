# Extracted from ./data/repos/pandas/pandas/tests/base/test_misc.py
# GH#41855 make sure its clear these are aliases
doc = pd.DataFrame.notnull.__doc__
assert doc.startswith("\nDataFrame.notnull is an alias for DataFrame.notna.\n")
doc = pd.DataFrame.isnull.__doc__
assert doc.startswith("\nDataFrame.isnull is an alias for DataFrame.isna.\n")

doc = Series.notnull.__doc__
assert doc.startswith("\nSeries.notnull is an alias for Series.notna.\n")
doc = Series.isnull.__doc__
assert doc.startswith("\nSeries.isnull is an alias for Series.isna.\n")
