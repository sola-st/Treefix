# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with context.eager_mode():
    t1 = constant_op.constant([1., 2.])
    t2 = constant_op.constant([1., 2.])
    x = check_ops.assert_near(t1, t2)
    assert x is None
