# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
renamer = lambda x: x.strftime("%Y%m%d")
expected = renamer(datetime_series.index[0])

datetime_series.rename(renamer, inplace=True)
assert datetime_series.index[0] == expected
