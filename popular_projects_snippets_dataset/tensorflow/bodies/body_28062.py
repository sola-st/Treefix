# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
with self.assertRaisesRegex(
    ValueError, r'Padded shape .* must be a `tf.int64` vector tensor, '
    r'but its shape was \(2, 2\).'):
    _ = dataset_ops.Dataset.from_tensors([1, 2, 3]).padded_batch(
        5, padded_shapes=[[1, 1], [1, 1]])
