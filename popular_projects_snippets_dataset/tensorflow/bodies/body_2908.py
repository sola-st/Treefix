# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
left_padding, _ = array_ops.SplitV(
    value=lhs, size_splits=[rhs, -1], axis=0, num_split=2)
_, right_padding = array_ops.SplitV(
    value=lhs, size_splits=[rhs, rhs], axis=1, num_split=2)
exit([left_padding, right_padding])
