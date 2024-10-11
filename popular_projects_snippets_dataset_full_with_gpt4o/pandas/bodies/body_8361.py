# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
pd.bdate_range(
    "1/1/2005", "1/1/2009", freq="C", tz=dateutil.tz.tzutc()
)._summary()
