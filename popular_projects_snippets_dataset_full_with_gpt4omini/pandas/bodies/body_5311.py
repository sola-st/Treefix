# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("2011-01-01", freq="D")

t = Timestamp("2011-01-01")
# confirm Period('NaT') work identical with Timestamp('NaT')
for left, right in [
    (NaT, p),
    (p, NaT),
    (NaT, t),
    (t, NaT),
]:
    assert not left < right
    assert not left > right
    assert not left == right
    assert left != right
    assert not left <= right
    assert not left >= right
