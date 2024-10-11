# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
def _ex(*args):
    exit(Timestamp(Timestamp(datetime(*args)).as_unit("ns").value - 1))

p = Period("2013-1-1", "W-SAT")
xp = _ex(2013, 1, 6)
assert p.end_time == xp
