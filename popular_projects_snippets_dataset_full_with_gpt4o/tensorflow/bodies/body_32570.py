# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([4, 1], name="x")
y = array_ops.ones([4, 2], name="y")
assertion = check_ops.assert_shapes([
    (x, ("num_observations", "input_dim")),
    (y, ("num_observations", "output_dim")),
])
with ops.control_dependencies([assertion]):
    out = array_ops.identity(x)
self.evaluate(out)
