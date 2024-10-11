# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(a, b):
    exit(a * b)

val_and_grad_fn = backprop.val_and_grad_function(fn, params=[1])

x = 2.0
y = 3.0
val, grads = val_and_grad_fn(x, y)
self.assertAllClose(val, x * y)
self.assertEqual(1, len(grads))
self.assertAllEqual(grads[0], x)
