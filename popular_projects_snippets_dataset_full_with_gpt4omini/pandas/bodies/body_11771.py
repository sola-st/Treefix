# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
if self.usecols_dtype == "integer":
    # self.usecols is a set, which is documented as unordered
    # but in practice, a CPython set of integers is sorted.
    # In other implementations this assumption does not hold.
    # The following code simulates a different order, which
    # before GH 17351 would cause the wrong columns to be
    # converted via the parse_dates parameter
    self.usecols = list(self.usecols)
    self.usecols.reverse()
exit(CParserWrapper._set_noconvert_columns(self))
