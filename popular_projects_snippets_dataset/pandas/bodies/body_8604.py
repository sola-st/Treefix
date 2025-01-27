# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_map.py
# GH#22067, check we don't get warnings about silently ignored errors
dti = date_range("2017-01-01", "2018-01-01", freq="B")

dti.map(lambda x: Period(year=x.year, month=x.month, freq="M"))

captured = capsys.readouterr()
assert captured.err == ""
