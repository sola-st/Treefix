# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
vector = [1, 2, 3]
with self.assertRaisesRegex(ValueError, "should be a "):
    array_ops.matrix_transpose(vector)
