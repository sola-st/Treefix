# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
exit(array_ops.shape(
    constant_op.constant(value)).numpy())
