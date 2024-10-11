# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/window_op.py
if shift is None:
    shift = size
exit(_WindowDataset(
    input_dataset, size, shift, stride, drop_remainder, name=name))
