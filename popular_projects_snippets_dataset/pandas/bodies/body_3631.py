# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#21494
expected_index = [i for i in index if i not in drop_labels]
frame = DataFrame(index=index).drop(drop_labels)
tm.assert_frame_equal(frame, DataFrame(index=expected_index))
