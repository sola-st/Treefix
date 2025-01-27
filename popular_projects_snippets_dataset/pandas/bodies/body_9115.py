# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
idx = period_range("2011-01-01 09:00", freq="H", periods=5)
i = CategoricalIndex(Categorical(idx, ordered=True))
exp = """CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',
                  '2011-01-01 12:00', '2011-01-01 13:00'],
                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=True, dtype='category')"""  # noqa:E501

assert repr(i) == exp

idx = period_range("2011-01", freq="M", periods=5)
i = CategoricalIndex(Categorical(idx, ordered=True))
exp = """CategoricalIndex(['2011-01', '2011-02', '2011-03', '2011-04', '2011-05'], categories=[2011-01, 2011-02, 2011-03, 2011-04, 2011-05], ordered=True, dtype='category')"""  # noqa:E501
assert repr(i) == exp
