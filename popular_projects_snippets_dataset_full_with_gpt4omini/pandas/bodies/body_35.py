# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# GH 35964
other_axis = 1 if axis in {0, "index"} else 0
with np.errstate(all="ignore"):
    expected = zip_frames([op(float_frame) for op in ops], axis=other_axis)
if axis in {0, "index"}:
    expected.columns = MultiIndex.from_product([float_frame.columns, names])
else:
    expected.index = MultiIndex.from_product([float_frame.index, names])
result = float_frame.transform(ops, axis=axis)
tm.assert_frame_equal(result, expected)
