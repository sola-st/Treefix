# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_formats.py
# GH#7601
idx1 = PeriodIndex([], freq="D")
idx2 = PeriodIndex(["2011-01-01"], freq="D")
idx3 = PeriodIndex(["2011-01-01", "2011-01-02"], freq="D")
idx4 = PeriodIndex(["2011-01-01", "2011-01-02", "2011-01-03"], freq="D")
idx5 = PeriodIndex(["2011", "2012", "2013"], freq="A")
idx6 = PeriodIndex(["2011-01-01 09:00", "2012-02-01 10:00", "NaT"], freq="H")
idx7 = pd.period_range("2013Q1", periods=1, freq="Q")
idx8 = pd.period_range("2013Q1", periods=2, freq="Q")
idx9 = pd.period_range("2013Q1", periods=3, freq="Q")
idx10 = PeriodIndex(["2011-01-01", "2011-02-01"], freq="3D")

exp1 = "PeriodIndex([], dtype='period[D]')"

exp2 = "PeriodIndex(['2011-01-01'], dtype='period[D]')"

exp3 = "PeriodIndex(['2011-01-01', '2011-01-02'], dtype='period[D]')"

exp4 = (
    "PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03'], "
    "dtype='period[D]')"
)

exp5 = "PeriodIndex(['2011', '2012', '2013'], dtype='period[A-DEC]')"

exp6 = (
    "PeriodIndex(['2011-01-01 09:00', '2012-02-01 10:00', 'NaT'], "
    "dtype='period[H]')"
)

exp7 = "PeriodIndex(['2013Q1'], dtype='period[Q-DEC]')"

exp8 = "PeriodIndex(['2013Q1', '2013Q2'], dtype='period[Q-DEC]')"

exp9 = "PeriodIndex(['2013Q1', '2013Q2', '2013Q3'], dtype='period[Q-DEC]')"

exp10 = "PeriodIndex(['2011-01-01', '2011-02-01'], dtype='period[3D]')"

for idx, expected in zip(
    [idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9, idx10],
    [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10],
):
    result = getattr(idx, method)()
    assert result == expected
