# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
# test all length
idx = period_range("2011-01-01 09:00", freq="H", periods=1)
i = CategoricalIndex(Categorical(idx))
exp = """CategoricalIndex(['2011-01-01 09:00'], categories=[2011-01-01 09:00], ordered=False, dtype='category')"""  # noqa:E501
assert repr(i) == exp

idx = period_range("2011-01-01 09:00", freq="H", periods=2)
i = CategoricalIndex(Categorical(idx))
exp = """CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00], ordered=False, dtype='category')"""  # noqa:E501
assert repr(i) == exp

idx = period_range("2011-01-01 09:00", freq="H", periods=3)
i = CategoricalIndex(Categorical(idx))
exp = """CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00], ordered=False, dtype='category')"""  # noqa:E501
assert repr(i) == exp

idx = period_range("2011-01-01 09:00", freq="H", periods=5)
i = CategoricalIndex(Categorical(idx))
exp = """CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',
                  '2011-01-01 12:00', '2011-01-01 13:00'],
                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"""  # noqa:E501

assert repr(i) == exp

i = CategoricalIndex(Categorical(idx.append(idx)))
exp = """CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',
                  '2011-01-01 12:00', '2011-01-01 13:00', '2011-01-01 09:00',
                  '2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00',
                  '2011-01-01 13:00'],
                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"""  # noqa:E501

assert repr(i) == exp

idx = period_range("2011-01", freq="M", periods=5)
i = CategoricalIndex(Categorical(idx))
exp = """CategoricalIndex(['2011-01', '2011-02', '2011-03', '2011-04', '2011-05'], categories=[2011-01, 2011-02, 2011-03, 2011-04, 2011-05], ordered=False, dtype='category')"""  # noqa:E501
assert repr(i) == exp
