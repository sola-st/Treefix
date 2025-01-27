# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
idx = date_range("2011-01-01 09:00", freq="H", periods=5)
s = Series(Categorical(idx))
exp = """0   2011-01-01 09:00:00
1   2011-01-01 10:00:00
2   2011-01-01 11:00:00
3   2011-01-01 12:00:00
4   2011-01-01 13:00:00
dtype: category
Categories (5, datetime64[ns]): [2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00,
                                 2011-01-01 12:00:00, 2011-01-01 13:00:00]"""  # noqa:E501

assert repr(s) == exp

idx = date_range("2011-01-01 09:00", freq="H", periods=5, tz="US/Eastern")
s = Series(Categorical(idx))
exp = """0   2011-01-01 09:00:00-05:00
1   2011-01-01 10:00:00-05:00
2   2011-01-01 11:00:00-05:00
3   2011-01-01 12:00:00-05:00
4   2011-01-01 13:00:00-05:00
dtype: category
Categories (5, datetime64[ns, US/Eastern]): [2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00,
                                             2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00,
                                             2011-01-01 13:00:00-05:00]"""  # noqa:E501

assert repr(s) == exp
