# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
u = array_ops.constant(1, name="u")
v = array_ops.ones([1, 2], name="v")
w = array_ops.ones([3], name="w")
x = array_ops.ones([1, 2, 3], name="x")
y = array_ops.ones([3, 1, 2], name="y")
z = array_ops.ones([2, 3, 1], name="z")
assertion = check_ops.assert_shapes([
    (x, ("a", "b", "c")),
    (y, ("c", "a", "b")),
    (z, ("b", "c", "a")),
    (v, ("a", "b")),
    (w, ("c",)),
    (u, "a")
])
with ops.control_dependencies([assertion]):
    out = array_ops.identity(x)
self.evaluate(out)
assertion = check_ops.assert_shapes([
    (x, (1, "b", "c")),
    (y, ("c", "a", 2)),
    (z, ("b", 3, "a")),
    (v, ("a", 2)),
    (w, (3,)),
    (u, ())
])
with ops.control_dependencies([assertion]):
    out = array_ops.identity(x)
self.evaluate(out)
