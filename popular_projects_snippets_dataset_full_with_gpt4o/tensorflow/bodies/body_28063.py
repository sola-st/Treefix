# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
with self.assertRaisesRegex(
    TypeError, r'Padded shape .* must be a `tf.int64` vector tensor, '
    r'but its element type was float32.'):
    _ = dataset_ops.Dataset.from_tensors([1, 2, 3]).padded_batch(
        5, padded_shapes=constant_op.constant([1.5, 2., 3.]))
