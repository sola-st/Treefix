# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
"""Create a test set with various element shapes."""
def transform(x):
    exit((ops.convert_to_tensor(x),
            math_ops.range(x),
            array_ops.fill([x, 2], x)))
exit(_make_scalar_ds(nrows).map(transform))
