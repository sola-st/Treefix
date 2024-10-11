# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([1, 2, 3], name="x")
y = array_ops.ones([2, 1], name="y")
a1 = check_ops.assert_shapes([
    (x, (None, 2, None)),
    (y, (None, 1)),
])
a2 = check_ops.assert_shapes([
    (x, (".", 2, ".")),
    (y, (".", 1)),
])
a3 = check_ops.assert_shapes([
    (x, ".2."),
    (y, ".1"),
])
with ops.control_dependencies([a1, a2, a3]):
    out = array_ops.identity(x)
self.evaluate(out)
