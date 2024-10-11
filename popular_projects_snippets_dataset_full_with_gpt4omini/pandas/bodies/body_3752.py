# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
# mixed floats/ints
other = DataFrame(index=range(5), columns=["A", "B", "C"])

af, bf = mixed_float_frame.align(
    other.iloc[:, 0], join="inner", axis=1, method=None, fill_value=0
)
tm.assert_index_equal(bf.index, Index([]))
