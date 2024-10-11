# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = constant_op.constant([1, 1, 1, 1, 1])
with self.assertRaises(ValueError):
    _ = dropout_fn(x, rate=0.5)
