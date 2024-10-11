# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
idx = timedelta_range("1 days", periods=5)
i = CategoricalIndex(Categorical(idx))
exp = """CategoricalIndex(['1 days', '2 days', '3 days', '4 days', '5 days'], categories=[1 days, 2 days, 3 days, 4 days, 5 days], ordered=False, dtype='category')"""  # noqa:E501
assert repr(i) == exp

idx = timedelta_range("1 hours", periods=10)
i = CategoricalIndex(Categorical(idx))
exp = """CategoricalIndex(['0 days 01:00:00', '1 days 01:00:00', '2 days 01:00:00',
                  '3 days 01:00:00', '4 days 01:00:00', '5 days 01:00:00',
                  '6 days 01:00:00', '7 days 01:00:00', '8 days 01:00:00',
                  '9 days 01:00:00'],
                 categories=[0 days 01:00:00, 1 days 01:00:00, 2 days 01:00:00, 3 days 01:00:00, ..., 6 days 01:00:00, 7 days 01:00:00, 8 days 01:00:00, 9 days 01:00:00], ordered=False, dtype='category')"""  # noqa:E501

assert repr(i) == exp
