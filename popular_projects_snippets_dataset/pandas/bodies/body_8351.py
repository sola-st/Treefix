# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
idxs = []
idxs.append(DatetimeIndex([], freq="D"))
idxs.append(DatetimeIndex(["2011-01-01"], freq="D"))
idxs.append(DatetimeIndex(["2011-01-01", "2011-01-02"], freq="D"))
idxs.append(DatetimeIndex(["2011-01-01", "2011-01-02", "2011-01-03"], freq="D"))
idxs.append(
    DatetimeIndex(
        ["2011-01-01 09:00", "2011-01-01 10:00", "2011-01-01 11:00"],
        freq="H",
        tz="Asia/Tokyo",
    )
)
idxs.append(
    DatetimeIndex(
        ["2011-01-01 09:00", "2011-01-01 10:00", pd.NaT], tz="US/Eastern"
    )
)
idxs.append(
    DatetimeIndex(["2011-01-01 09:00", "2011-01-01 10:00", pd.NaT], tz="UTC")
)

exp = []
exp.append("DatetimeIndex([], dtype='datetime64[ns]', freq='D')")
exp.append("DatetimeIndex(['2011-01-01'], dtype='datetime64[ns]', freq='D')")
exp.append(
    "DatetimeIndex(['2011-01-01', '2011-01-02'], "
    "dtype='datetime64[ns]', freq='D')"
)
exp.append(
    "DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], "
    "dtype='datetime64[ns]', freq='D')"
)
exp.append(
    "DatetimeIndex(['2011-01-01 09:00:00+09:00', "
    "'2011-01-01 10:00:00+09:00', '2011-01-01 11:00:00+09:00']"
    ", dtype='datetime64[ns, Asia/Tokyo]', freq='H')"
)
exp.append(
    "DatetimeIndex(['2011-01-01 09:00:00-05:00', "
    "'2011-01-01 10:00:00-05:00', 'NaT'], "
    "dtype='datetime64[ns, US/Eastern]', freq=None)"
)
exp.append(
    "DatetimeIndex(['2011-01-01 09:00:00+00:00', "
    "'2011-01-01 10:00:00+00:00', 'NaT'], "
    "dtype='datetime64[ns, UTC]', freq=None)"
    ""
)

with pd.option_context("display.width", 300):
    for indx, expected in zip(idxs, exp):
        result = getattr(indx, method)()
        assert result == expected
