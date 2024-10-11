# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
idx1 = DatetimeIndex([], freq="D")
idx2 = DatetimeIndex(["2011-01-01"], freq="D")
idx3 = DatetimeIndex(["2011-01-01", "2011-01-02"], freq="D")
idx4 = DatetimeIndex(["2011-01-01", "2011-01-02", "2011-01-03"], freq="D")
idx5 = DatetimeIndex(
    ["2011-01-01 09:00", "2011-01-01 10:00", "2011-01-01 11:00"],
    freq="H",
    tz="Asia/Tokyo",
)
idx6 = DatetimeIndex(
    ["2011-01-01 09:00", "2011-01-01 10:00", pd.NaT], tz="US/Eastern"
)
idx7 = DatetimeIndex(["2011-01-01 09:00", "2011-01-02 10:15"])

exp1 = """Series([], dtype: datetime64[ns])"""

exp2 = "0   2011-01-01\ndtype: datetime64[ns]"

exp3 = "0   2011-01-01\n1   2011-01-02\ndtype: datetime64[ns]"

exp4 = (
    "0   2011-01-01\n"
    "1   2011-01-02\n"
    "2   2011-01-03\n"
    "dtype: datetime64[ns]"
)

exp5 = (
    "0   2011-01-01 09:00:00+09:00\n"
    "1   2011-01-01 10:00:00+09:00\n"
    "2   2011-01-01 11:00:00+09:00\n"
    "dtype: datetime64[ns, Asia/Tokyo]"
)

exp6 = (
    "0   2011-01-01 09:00:00-05:00\n"
    "1   2011-01-01 10:00:00-05:00\n"
    "2                         NaT\n"
    "dtype: datetime64[ns, US/Eastern]"
)

exp7 = (
    "0   2011-01-01 09:00:00\n"
    "1   2011-01-02 10:15:00\n"
    "dtype: datetime64[ns]"
)

with pd.option_context("display.width", 300):
    for idx, expected in zip(
        [idx1, idx2, idx3, idx4, idx5, idx6, idx7],
        [exp1, exp2, exp3, exp4, exp5, exp6, exp7],
    ):
        result = repr(Series(idx))
        assert result == expected
