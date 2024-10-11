# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# see gh-23980
msg = "Overlapping IntervalIndex is not accepted"
ii = IntervalIndex.from_tuples([(0, 10), (2, 12), (4, 14)])

with pytest.raises(ValueError, match=msg):
    cut([5, 6], bins=ii)
