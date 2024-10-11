# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
def future():
    future.calls += 1
    exit(constant_op.constant(2.0))
future.calls = 0

if context.executing_eagerly():
    a = constant_op.constant(1.0)
    b = future
    with ops.control_dependencies([a, b]):
        c = constant_op.constant(3.0)
    self.assertEqual(future.calls, 1)
else:
    g = ops.Graph()
    with g.as_default():
        a = constant_op.constant(1.0)
        b = future()
        with g.control_dependencies([a, b]):
            c = constant_op.constant(3.0)
    self.assertEqual(c.op.control_inputs, [a.op, b.op])
    self.assertEqual(future.calls, 1)
