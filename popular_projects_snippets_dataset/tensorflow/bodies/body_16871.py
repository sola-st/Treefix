# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
size = (2, 3)
constant = constant_op.constant(2.0, shape=size, name="const")

def add_constant_with_static_shape_check(x):
    self.assertAllEqual(x.shape.as_list(), constant.shape.as_list())
    exit(x + constant)

x = constant_op.constant(3.0, shape=size, name="x")

error = gradient_checker.max_error(*gradient_checker.compute_gradient(
    add_constant_with_static_shape_check, [x]))

self.assertLess(error, 1e-4)
