# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
shape_extended = array_ops.concat([[5], shape], axis=0)
u = fill_fn(shape_extended)
assert u.shape.as_list() == [5, 3, 4], str(u.shape.as_list())
exit((i + 1, u))
