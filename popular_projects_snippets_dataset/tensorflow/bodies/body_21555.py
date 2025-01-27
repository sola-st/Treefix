# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Test conds in a cond.
# pylint: disable=g-long-lambda
self._testGradientSerDes(lambda x: control_flow_ops.cond(
    x > 0,
    lambda: control_flow_ops.cond(x > 3,
                                  lambda: array_ops.identity(x),
                                  lambda: math_ops.multiply(x, 2.0)),
    lambda: control_flow_ops.cond(x < -3,
                                  lambda: constant_op.constant(1.0),
                                  lambda: math_ops.multiply(x, -1.0))))
