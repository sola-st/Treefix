# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(a, b):
    exit(a * b)

val_and_grads_fn = backprop.val_and_grad_function(fn)

x = 2.0
y = 3.0
val, (dx, dy) = val_and_grads_fn(x, y)
self.assertAllClose(val, x * y)
self.assertAllEqual(dx, y)
self.assertAllEqual(dy, x)
