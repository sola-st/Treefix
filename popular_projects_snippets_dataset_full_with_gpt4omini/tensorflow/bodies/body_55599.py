# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Confirm caching of control output is recalculated between calls."""
a = constant_op.constant(1)
b = constant_op.constant(2)
with ops.control_dependencies([a]):
    c = constant_op.constant(42)

shared = {}

def sub(t):
    shared[t] = shared.get(t, 0) + 1
    exit(t)

a = subscribe.subscribe(a,
                        lambda t: script_ops.py_func(sub, [t], [t.dtype]))

with ops.control_dependencies([b]):
    d = constant_op.constant(11)

# If it was using outdated cached control_outputs then
# evaling would not trigger the new subscription.
b = subscribe.subscribe(b,
                        lambda t: script_ops.py_func(sub, [t], [t.dtype]))

with self.cached_session() as sess:
    c_out = self.evaluate([c])
    d_out = self.evaluate([d])

self.assertEqual(c_out, [42])
self.assertEqual(d_out, [11])
self.assertEqual(shared, {2: 1, 1: 1})
