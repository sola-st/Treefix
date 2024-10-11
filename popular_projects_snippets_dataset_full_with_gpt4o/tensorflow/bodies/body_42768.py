# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
l = [array_ops.zeros((10, 1)).numpy(), array_ops.zeros(1).numpy()]

with self.assertRaisesRegex(ValueError, "non-rectangular Python sequence"):
    constant_op.constant(l)
