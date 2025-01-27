# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
ts = datetime_series
renamer = lambda x: x.strftime("%Y%m%d")
renamed = ts.rename(renamer)
assert renamed.index[0] == renamer(ts.index[0])

# dict
rename_dict = dict(zip(ts.index, renamed.index))
renamed2 = ts.rename(rename_dict)
tm.assert_series_equal(renamed, renamed2)
