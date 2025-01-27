# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
input_tensor = array_ops.constant([[1]])
with self.assertRaisesRegex(ValueError, "Dimension -2 must be >= 0"):
    dataset_ops.Dataset.from_tensors(input_tensor).sparse_batch(4, [-2])
