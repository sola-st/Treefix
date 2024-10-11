# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
# GH#9116
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

exp1 = "DatetimeIndex: 0 entries\nFreq: D"

exp2 = "DatetimeIndex: 1 entries, 2011-01-01 to 2011-01-01\nFreq: D"

exp3 = "DatetimeIndex: 2 entries, 2011-01-01 to 2011-01-02\nFreq: D"

exp4 = "DatetimeIndex: 3 entries, 2011-01-01 to 2011-01-03\nFreq: D"

exp5 = (
    "DatetimeIndex: 3 entries, 2011-01-01 09:00:00+09:00 "
    "to 2011-01-01 11:00:00+09:00\n"
    "Freq: H"
)

exp6 = """DatetimeIndex: 3 entries, 2011-01-01 09:00:00-05:00 to NaT"""

for idx, expected in zip(
    [idx1, idx2, idx3, idx4, idx5, idx6], [exp1, exp2, exp3, exp4, exp5, exp6]
):
    result = idx._summary()
    assert result == expected
