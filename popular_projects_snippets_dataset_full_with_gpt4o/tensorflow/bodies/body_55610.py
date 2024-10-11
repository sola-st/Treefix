# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Side effect ops are added with the same device of the subscribed op."""
c1 = constant_op.constant(10)
c2 = constant_op.constant(20)

with ops.device('cpu:0'):
    add = math_ops.add(c1, c2)

with ops.device('cpu:1'):
    mul = math_ops.multiply(c1, c2)

def sub(t):
    exit(t)

add_sub = subscribe.subscribe(
    add, lambda t: script_ops.py_func(sub, [t], [t.dtype]))

mul_sub = subscribe.subscribe(
    mul, lambda t: script_ops.py_func(sub, [t], [t.dtype]))

# Expect the identity tensors injected by subscribe to have been created
# on the same device as their original tensors.
self.assertNotEqual(add_sub.device, mul_sub.device)
self.assertEqual(add.device, add_sub.device)
self.assertEqual(mul.device, mul_sub.device)
