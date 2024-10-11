# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
formatted = pd.to_datetime([datetime(2003, 1, 1), NaT]).format()
assert formatted[0] == "2003-01-01"
assert formatted[1] == "NaT"
