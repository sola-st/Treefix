# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    # Creating unregistered ops with _apply_op() doesn't work with the C API
    # TODO(skyewm): address this more consistently. Possible solutions are
    # to use registered ops in all tests, create a way to register ops in
    # Python tests, or conditionally disable the op registration check in
    # the C API.
    a = constant_op.constant(1.0)
    b = constant_op.constant(1.0)
    with g.control_dependencies([a]):
        c = constant_op.constant(1.0)
        d = array_ops.identity(b)
        e = array_ops.identity(c)

self.assertEqual(c.op.control_inputs, [a.op])
self.assertEqual(d.op.control_inputs, [a.op])
# e should be dominated by c.
self.assertEqual(e.op.control_inputs, [])
