# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
with self.assertRaises(TypeError):
    _ = constant_op.constant(0) < 0.5
