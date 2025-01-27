# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
idx = period_range("2011-01-01 09:00", freq="H", periods=5)
s = Series(Categorical(idx, ordered=True))
exp = """0    2011-01-01 09:00
1    2011-01-01 10:00
2    2011-01-01 11:00
3    2011-01-01 12:00
4    2011-01-01 13:00
dtype: category
Categories (5, period[H]): [2011-01-01 09:00 < 2011-01-01 10:00 < 2011-01-01 11:00 < 2011-01-01 12:00 <
                            2011-01-01 13:00]"""  # noqa:E501

assert repr(s) == exp

idx = period_range("2011-01", freq="M", periods=5)
s = Series(Categorical(idx, ordered=True))
exp = """0    2011-01
1    2011-02
2    2011-03
3    2011-04
4    2011-05
dtype: category
Categories (5, period[M]): [2011-01 < 2011-02 < 2011-03 < 2011-04 < 2011-05]"""

assert repr(s) == exp
