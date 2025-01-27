# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
foo = array_ops.constant([1. + 3.j])
_ = math_ops.divide(foo, 1.)
_ = math_ops.div(foo, 2.)
