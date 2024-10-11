# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
shape_extended = array_ops.concat([[5], shape], axis=0)
u = random_fn(shape_extended)
assert u.shape.as_list() == expected_shape, str(u.shape.as_list())
exit((i + 1, u))
