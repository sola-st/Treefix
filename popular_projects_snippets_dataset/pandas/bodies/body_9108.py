# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
idx = timedelta_range("1 days", periods=5)
c = Categorical(idx)
exp = """[1 days, 2 days, 3 days, 4 days, 5 days]
Categories (5, timedelta64[ns]): [1 days, 2 days, 3 days, 4 days, 5 days]"""

assert repr(c) == exp

c = Categorical(idx.append(idx), categories=idx)
exp = """[1 days, 2 days, 3 days, 4 days, 5 days, 1 days, 2 days, 3 days, 4 days, 5 days]
Categories (5, timedelta64[ns]): [1 days, 2 days, 3 days, 4 days, 5 days]"""  # noqa:E501

assert repr(c) == exp

idx = timedelta_range("1 hours", periods=20)
c = Categorical(idx)
exp = """[0 days 01:00:00, 1 days 01:00:00, 2 days 01:00:00, 3 days 01:00:00, 4 days 01:00:00, ..., 15 days 01:00:00, 16 days 01:00:00, 17 days 01:00:00, 18 days 01:00:00, 19 days 01:00:00]
Length: 20
Categories (20, timedelta64[ns]): [0 days 01:00:00, 1 days 01:00:00, 2 days 01:00:00,
                                   3 days 01:00:00, ..., 16 days 01:00:00, 17 days 01:00:00,
                                   18 days 01:00:00, 19 days 01:00:00]"""  # noqa:E501

assert repr(c) == exp

c = Categorical(idx.append(idx), categories=idx)
exp = """[0 days 01:00:00, 1 days 01:00:00, 2 days 01:00:00, 3 days 01:00:00, 4 days 01:00:00, ..., 15 days 01:00:00, 16 days 01:00:00, 17 days 01:00:00, 18 days 01:00:00, 19 days 01:00:00]
Length: 40
Categories (20, timedelta64[ns]): [0 days 01:00:00, 1 days 01:00:00, 2 days 01:00:00,
                                   3 days 01:00:00, ..., 16 days 01:00:00, 17 days 01:00:00,
                                   18 days 01:00:00, 19 days 01:00:00]"""  # noqa:E501

assert repr(c) == exp
