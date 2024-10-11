# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# with dict of empty list and Series
frame = DataFrame({"A": [], "B": []}, columns=["A", "B"])
tm.assert_index_equal(frame.index, RangeIndex(0), exact=True)
