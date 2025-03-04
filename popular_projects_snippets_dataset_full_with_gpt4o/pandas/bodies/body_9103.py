# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
idx = date_range("2011-01-01 09:00", freq="H", periods=5)
c = Categorical(idx)

exp = (
    "[2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00, "
    "2011-01-01 12:00:00, 2011-01-01 13:00:00]\n"
    "Categories (5, datetime64[ns]): [2011-01-01 09:00:00, "
    "2011-01-01 10:00:00, 2011-01-01 11:00:00,\n"
    "                                 2011-01-01 12:00:00, "
    "2011-01-01 13:00:00]"
    ""
)
assert repr(c) == exp

c = Categorical(idx.append(idx), categories=idx)
exp = (
    "[2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00, "
    "2011-01-01 12:00:00, 2011-01-01 13:00:00, 2011-01-01 09:00:00, "
    "2011-01-01 10:00:00, 2011-01-01 11:00:00, 2011-01-01 12:00:00, "
    "2011-01-01 13:00:00]\n"
    "Categories (5, datetime64[ns]): [2011-01-01 09:00:00, "
    "2011-01-01 10:00:00, 2011-01-01 11:00:00,\n"
    "                                 2011-01-01 12:00:00, "
    "2011-01-01 13:00:00]"
)

assert repr(c) == exp

idx = date_range("2011-01-01 09:00", freq="H", periods=5, tz="US/Eastern")
c = Categorical(idx)
exp = (
    "[2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00, "
    "2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00, "
    "2011-01-01 13:00:00-05:00]\n"
    "Categories (5, datetime64[ns, US/Eastern]): "
    "[2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00,\n"
    "                                             "
    "2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00,\n"
    "                                             "
    "2011-01-01 13:00:00-05:00]"
)

assert repr(c) == exp

c = Categorical(idx.append(idx), categories=idx)
exp = (
    "[2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00, "
    "2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00, "
    "2011-01-01 13:00:00-05:00, 2011-01-01 09:00:00-05:00, "
    "2011-01-01 10:00:00-05:00, 2011-01-01 11:00:00-05:00, "
    "2011-01-01 12:00:00-05:00, 2011-01-01 13:00:00-05:00]\n"
    "Categories (5, datetime64[ns, US/Eastern]): "
    "[2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00,\n"
    "                                             "
    "2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00,\n"
    "                                             "
    "2011-01-01 13:00:00-05:00]"
)

assert repr(c) == exp
