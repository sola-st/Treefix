# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
tz = tz_naive_fixture
# monotonic
idx1 = DatetimeIndex(["2011-01-01", "2011-01-02", "2011-01-03"], tz=tz)
assert idx1.is_monotonic_increasing

# non-monotonic
idx2 = DatetimeIndex(
    ["2011-01-01", NaT, "2011-01-03", "2011-01-02", NaT], tz=tz
)
assert not idx2.is_monotonic_increasing

for idx in [idx1, idx2]:
    assert idx.min() == Timestamp("2011-01-01", tz=tz)
    assert idx.max() == Timestamp("2011-01-03", tz=tz)
    assert idx.argmin() == 0
    assert idx.argmax() == 2
