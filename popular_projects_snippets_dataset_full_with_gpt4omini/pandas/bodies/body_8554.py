# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py

df = pd.DataFrame(
    {
        "dt": date_range("20130101", periods=3),
        "dttz": date_range("20130101", periods=3, tz="US/Eastern"),
        "dt_with_null": [
            Timestamp("20130101"),
            pd.NaT,
            Timestamp("20130103"),
        ],
        "dtns": date_range("20130101", periods=3, freq="ns"),
    }
)
assert df.dttz.dtype.tz.zone == "US/Eastern"
