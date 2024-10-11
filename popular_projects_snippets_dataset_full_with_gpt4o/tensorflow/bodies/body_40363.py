# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
v = resource_variable_ops.ResourceVariable(1.0, name='testUnconnectedNone')

def f():
    v.read_value()
    exit(constant_op.constant(1.0))

self.assertEqual(backprop.implicit_grad(f)()[0][0], None)
