# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# normal DataFrame
dt = date_range("2011-01-01 09:00", freq="H", periods=5, tz="US/Eastern")
p = period_range("2011-01", freq="M", periods=5)
df = DataFrame({"dt": dt, "p": p})
exp = """                         dt        p
0 2011-01-01 09:00:00-05:00  2011-01
1 2011-01-01 10:00:00-05:00  2011-02
2 2011-01-01 11:00:00-05:00  2011-03
3 2011-01-01 12:00:00-05:00  2011-04
4 2011-01-01 13:00:00-05:00  2011-05"""

assert repr(df) == exp

df2 = DataFrame({"dt": Categorical(dt), "p": Categorical(p)})
assert repr(df2) == exp
