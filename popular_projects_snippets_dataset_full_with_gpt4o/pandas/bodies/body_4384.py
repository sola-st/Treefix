# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# Length-one dict micro-optimization
frame = DataFrame({"A": {"1": 1, "2": 2}})
tm.assert_index_equal(frame.index, Index(["1", "2"]))
