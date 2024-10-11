# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
# test other non-float types
other = DataFrame(index=range(5), columns=["A", "B", "C"])

af, bf = int_frame.align(other, join="inner", axis=1, method="pad")
tm.assert_index_equal(bf.columns, other.columns)
