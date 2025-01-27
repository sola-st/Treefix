# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Confirm side effect are correctly added for different input types."""
a = constant_op.constant(1)
b = constant_op.constant(2)
c = math_ops.add(a, b)

shared = {}

def sub(t, name):
    shared[name] = shared.get(name, 0) + 1
    exit(t)

# Subscribe with a first side effect graph, passing an unsubscribed tensor.
sub_graph1 = lambda t: sub(t, 'graph1')
c_sub = subscribe.subscribe(
    c, lambda t: script_ops.py_func(sub_graph1, [t], [t.dtype]))

# Add a second side effect graph, passing the tensor returned by the
# previous call to subscribe().
sub_graph2 = lambda t: sub(t, 'graph2')
c_sub2 = subscribe.subscribe(
    c_sub, lambda t: script_ops.py_func(sub_graph2, [t], [t.dtype]))

# Add a third side effect graph, passing the original tensor.
sub_graph3 = lambda t: sub(t, 'graph3')
c_sub3 = subscribe.subscribe(
    c, lambda t: script_ops.py_func(sub_graph3, [t], [t.dtype]))

# Make sure there's only one identity op matching the source tensor's name.
graph_ops = ops.get_default_graph().get_operations()
name_prefix = c.op.name + '/subscription/Identity'
identity_ops = [op for op in graph_ops if op.name.startswith(name_prefix)]
self.assertEqual(1, len(identity_ops))

# Expect the objects returned by subscribe() to reference the same tensor.
self.assertIs(c_sub, c_sub2)
self.assertIs(c_sub, c_sub3)

# Expect the three side effect graphs to have been evaluated.
with self.cached_session() as sess:
    self.evaluate([c_sub])
self.assertIn('graph1', shared)
self.assertIn('graph2', shared)
self.assertIn('graph3', shared)
