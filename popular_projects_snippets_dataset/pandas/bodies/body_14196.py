# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
formatted = pd.to_datetime([datetime(2013, 1, 1)], utc=True).format()
assert formatted[0] == "2013-01-01 00:00:00+00:00"

formatted = pd.to_datetime([datetime(2013, 1, 1), NaT], utc=True).format()
assert formatted[0] == "2013-01-01 00:00:00+00:00"
