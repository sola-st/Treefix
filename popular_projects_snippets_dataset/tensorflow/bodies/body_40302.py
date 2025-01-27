# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x):
    exit(x + x)

int_tensor = constant_op.constant(1)
self.assertEqual(backprop.gradients_function(f)(int_tensor)[0], None)
