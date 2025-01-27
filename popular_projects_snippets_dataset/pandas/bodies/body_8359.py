# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
rng = pd.bdate_range(datetime(2009, 1, 1), datetime(2010, 1, 1), freq="C")
rng._summary()
rng[2:2]._summary()
