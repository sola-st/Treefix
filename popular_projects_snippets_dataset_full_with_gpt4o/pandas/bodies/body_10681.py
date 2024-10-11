# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_shift_diff.py
# GH 41264, single-index check
df = DataFrame(columns=["a", "b", "c"])
shifted = df.groupby(["a"]).shift(1)
shifted_with_fill = df.groupby(["a"]).shift(1, fill_value=0)
tm.assert_frame_equal(shifted, shifted_with_fill)
tm.assert_index_equal(shifted.index, shifted_with_fill.index)
