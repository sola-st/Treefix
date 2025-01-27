# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op_test.py
with self.assertRaises(TypeError):
    constant_op.constant("hello", dtype)
