# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant(1)
with self.assertRaises(ValueError):
    x.set_shape((1, 2))
