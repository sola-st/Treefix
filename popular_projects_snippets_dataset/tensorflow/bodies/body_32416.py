# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with context.eager_mode():
    small = constant_op.constant([1, 2], name="small")
    x = check_ops.assert_equal(small, small)
    assert x is None
