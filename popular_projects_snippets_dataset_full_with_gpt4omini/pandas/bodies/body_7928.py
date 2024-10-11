# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH 17717
p0 = Period("2017-09-01")
p1 = Period("2017-09-02")
p2 = Period("2017-09-03")

# get the location of p1/p2 from
# monotonic increasing PeriodIndex with non-duplicate
idx0 = PeriodIndex([p0, p1, p2])
expected_idx1_p1 = 1
expected_idx1_p2 = 2

assert idx0.get_loc(p1) == expected_idx1_p1
assert idx0.get_loc(str(p1)) == expected_idx1_p1
assert idx0.get_loc(p2) == expected_idx1_p2
assert idx0.get_loc(str(p2)) == expected_idx1_p2

msg = "Cannot interpret 'foo' as period"
with pytest.raises(KeyError, match=msg):
    idx0.get_loc("foo")
with pytest.raises(KeyError, match=r"^1\.1$"):
    idx0.get_loc(1.1)

with pytest.raises(InvalidIndexError, match=re.escape(str(idx0))):
    idx0.get_loc(idx0)

# get the location of p1/p2 from
# monotonic increasing PeriodIndex with duplicate
idx1 = PeriodIndex([p1, p1, p2])
expected_idx1_p1 = slice(0, 2)
expected_idx1_p2 = 2

assert idx1.get_loc(p1) == expected_idx1_p1
assert idx1.get_loc(str(p1)) == expected_idx1_p1
assert idx1.get_loc(p2) == expected_idx1_p2
assert idx1.get_loc(str(p2)) == expected_idx1_p2

msg = "Cannot interpret 'foo' as period"
with pytest.raises(KeyError, match=msg):
    idx1.get_loc("foo")

with pytest.raises(KeyError, match=r"^1\.1$"):
    idx1.get_loc(1.1)

with pytest.raises(InvalidIndexError, match=re.escape(str(idx1))):
    idx1.get_loc(idx1)

# get the location of p1/p2 from
# non-monotonic increasing/decreasing PeriodIndex with duplicate
idx2 = PeriodIndex([p2, p1, p2])
expected_idx2_p1 = 1
expected_idx2_p2 = np.array([True, False, True])

assert idx2.get_loc(p1) == expected_idx2_p1
assert idx2.get_loc(str(p1)) == expected_idx2_p1
tm.assert_numpy_array_equal(idx2.get_loc(p2), expected_idx2_p2)
tm.assert_numpy_array_equal(idx2.get_loc(str(p2)), expected_idx2_p2)
