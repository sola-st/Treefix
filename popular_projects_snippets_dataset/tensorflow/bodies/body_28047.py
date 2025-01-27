# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(([0, 1, 2, 3], None))
with self.assertRaises(TypeError):
    dataset = dataset.padded_batch(2)
