# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_formats.py
# GH#9116
idx1 = PeriodIndex([], freq="D")
idx2 = PeriodIndex(["2011-01-01"], freq="D")
idx3 = PeriodIndex(["2011-01-01", "2011-01-02"], freq="D")
idx4 = PeriodIndex(["2011-01-01", "2011-01-02", "2011-01-03"], freq="D")
idx5 = PeriodIndex(["2011", "2012", "2013"], freq="A")
idx6 = PeriodIndex(["2011-01-01 09:00", "2012-02-01 10:00", "NaT"], freq="H")

idx7 = pd.period_range("2013Q1", periods=1, freq="Q")
idx8 = pd.period_range("2013Q1", periods=2, freq="Q")
idx9 = pd.period_range("2013Q1", periods=3, freq="Q")

exp1 = """PeriodIndex: 0 entries
Freq: D"""

exp2 = """PeriodIndex: 1 entries, 2011-01-01 to 2011-01-01
Freq: D"""

exp3 = """PeriodIndex: 2 entries, 2011-01-01 to 2011-01-02
Freq: D"""

exp4 = """PeriodIndex: 3 entries, 2011-01-01 to 2011-01-03
Freq: D"""

exp5 = """PeriodIndex: 3 entries, 2011 to 2013
Freq: A-DEC"""

exp6 = """PeriodIndex: 3 entries, 2011-01-01 09:00 to NaT
Freq: H"""

exp7 = """PeriodIndex: 1 entries, 2013Q1 to 2013Q1
Freq: Q-DEC"""

exp8 = """PeriodIndex: 2 entries, 2013Q1 to 2013Q2
Freq: Q-DEC"""

exp9 = """PeriodIndex: 3 entries, 2013Q1 to 2013Q3
Freq: Q-DEC"""

for idx, expected in zip(
    [idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9],
    [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9],
):
    result = idx._summary()
    assert result == expected
