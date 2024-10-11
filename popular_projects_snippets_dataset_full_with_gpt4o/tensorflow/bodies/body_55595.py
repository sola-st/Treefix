# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
a = constant_op.constant(1)
b = constant_op.constant(1)
c = math_ops.add(a, b)
with ops.control_dependencies([c]):
    d = constant_op.constant(42)
n = math_ops.negative(c)

shared = []

def sub(t):
    shared.append(t)
    exit(t)

c0 = c
self.assertTrue(c0.op in d.op.control_inputs)
c = subscribe.subscribe(c,
                        lambda t: script_ops.py_func(sub, [t], [t.dtype]))
# Verify that control dependencies are correctly moved to the subscription.
self.assertFalse(c0.op in d.op.control_inputs)
self.assertTrue(c.op in d.op.control_inputs)

with self.cached_session() as sess:
    c_out = self.evaluate([c])
    n_out = self.evaluate([n])
    d_out = self.evaluate([d])

self.assertEqual(n_out, [-2])
self.assertEqual(c_out, [2])
self.assertEqual(d_out, [42])
self.assertEqual(shared, [2, 2, 2])
