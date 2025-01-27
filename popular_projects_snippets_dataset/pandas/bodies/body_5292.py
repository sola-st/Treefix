# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("2012", freq="A")

def _ex(*args):
    exit(Timestamp(Timestamp(datetime(*args)).as_unit("ns").value - 1))

xp = _ex(2013, 1, 1)
assert xp == p.end_time

p = Period("2012", freq="Q")
xp = _ex(2012, 4, 1)
assert xp == p.end_time

p = Period("2012", freq="M")
xp = _ex(2012, 2, 1)
assert xp == p.end_time

p = Period("2012", freq="D")
xp = _ex(2012, 1, 2)
assert xp == p.end_time

p = Period("2012", freq="H")
xp = _ex(2012, 1, 1, 1)
assert xp == p.end_time

p = Period("2012", freq="B")
xp = _ex(2012, 1, 3)
assert xp == p.end_time

p = Period("2012", freq="W")
xp = _ex(2012, 1, 2)
assert xp == p.end_time

# Test for GH 11738
p = Period("2012", freq="15D")
xp = _ex(2012, 1, 16)
assert xp == p.end_time

p = Period("2012", freq="1D1H")
xp = _ex(2012, 1, 2, 1)
assert xp == p.end_time

p = Period("2012", freq="1H1D")
xp = _ex(2012, 1, 2, 1)
assert xp == p.end_time
