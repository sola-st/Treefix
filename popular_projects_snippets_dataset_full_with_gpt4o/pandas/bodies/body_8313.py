# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# empty same freq GH2129
tz = tz_aware_fixture
rng = date_range("6/1/2000", "6/15/2000", freq=freq, tz=tz)
result = rng[0:0].intersection(rng)
assert len(result) == 0
assert result.freq == rng.freq

result = rng.intersection(rng[0:0])
assert len(result) == 0
assert result.freq == rng.freq

# no overlap GH#33604
check_freq = freq != "T"  # We don't preserve freq on non-anchored offsets
result = rng[:3].intersection(rng[-3:])
tm.assert_index_equal(result, rng[:0])
if check_freq:
    # We don't preserve freq on non-anchored offsets
    assert result.freq == rng.freq

# swapped left and right
result = rng[-3:].intersection(rng[:3])
tm.assert_index_equal(result, rng[:0])
if check_freq:
    # We don't preserve freq on non-anchored offsets
    assert result.freq == rng.freq
