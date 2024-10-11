# Extracted from ./data/repos/pandas/pandas/tests/series/test_subclass.py
sub_series = tm.SubclassedSeries()
assert "SubclassedSeries" in repr(sub_series)
