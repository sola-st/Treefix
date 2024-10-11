# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py

df = pd.DataFrame(
    {
        "string": list("abc"),
        "int": list(range(1, 4)),
        "uint": np.arange(3, 6).astype("u1"),
        "float": np.arange(4.0, 7.0, dtype="float64"),
        "float_with_null": [1.0, np.nan, 3],
        "bool": [True, False, True],
        "bool_with_null": [True, np.nan, False],
        "cat": pd.Categorical(list("abc")),
        "dt": pd.DatetimeIndex(
            list(pd.date_range("20130101", periods=3)), freq=None
        ),
        "dttz": pd.DatetimeIndex(
            list(pd.date_range("20130101", periods=3, tz="US/Eastern")),
            freq=None,
        ),
        "dt_with_null": [
            pd.Timestamp("20130101"),
            pd.NaT,
            pd.Timestamp("20130103"),
        ],
        "dtns": pd.DatetimeIndex(
            list(pd.date_range("20130101", periods=3, freq="ns")), freq=None
        ),
    }
)
df["periods"] = pd.period_range("2013", freq="M", periods=3)
df["timedeltas"] = pd.timedelta_range("1 day", periods=3)
df["intervals"] = pd.interval_range(0, 3, 3)

assert df.dttz.dtype.tz.zone == "US/Eastern"
self.check_round_trip(df)
