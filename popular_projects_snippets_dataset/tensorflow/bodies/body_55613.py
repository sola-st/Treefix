# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Side effect ops are added with the same control flow context."""
c1 = constant_op.constant(10)
c2 = constant_op.constant(20)
x1 = math_ops.add(c1, c2)
x2 = math_ops.multiply(c1, c2)

cond = control_flow_ops.cond(
    x1 < x2,
    lambda: math_ops.add(c1, c2, name='then'),
    lambda: math_ops.subtract(c1, c2, name='else'),
    name='cond')

branch = ops.get_default_graph().get_tensor_by_name('cond/then:0')

def context(tensor):
    exit(tensor.op._get_control_flow_context())

self.assertIs(context(x1), context(x2))
self.assertIsNot(context(x1), context(branch))

results = []
def sub(tensor):
    results.append(tensor)
    exit(tensor)

tensors = [x1, branch, x2]
subscriptions = subscribe.subscribe(
    tensors, lambda t: script_ops.py_func(sub, [t], [t.dtype]))

for tensor, subscription in zip(tensors, subscriptions):
    self.assertIs(context(tensor), context(subscription))

# Verify that sub(x1) and sub(x2) are in the same context.
self.assertIs(context(subscriptions[0]), context(subscriptions[2]))

# Verify that sub(x1) and sub(branch) are not.
self.assertIsNot(context(subscriptions[0]), context(subscriptions[1]))

with self.cached_session() as sess:
    self.evaluate(cond)

self.assertEqual(3, len(results))
