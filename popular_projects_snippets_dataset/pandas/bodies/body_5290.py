# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
freq_lst = ["A", "Q", "M", "D", "H", "T", "S"]
xp = datetime(2012, 1, 1)
for f in freq_lst:
    p = Period("2012", freq=f)
    assert p.start_time == xp
assert Period("2012", freq="B").start_time == datetime(2012, 1, 2)
assert Period("2012", freq="W").start_time == datetime(2011, 12, 26)
