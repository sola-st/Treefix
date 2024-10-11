# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

rt = ragged_tensor_value.RaggedTensorValue(
    np.array([0, 42]), np.array([0, 2], dtype=np.int64))

with self.assertRaisesRegex(
    TypeError, r'`padded_batch` is only supported for '
    r'datasets that produce tensor elements but type spec of elements in '
    r'the input dataset is not a subclass of TensorSpec: '
    r'`RaggedTensorSpec.*`\.$'):
    _ = dataset_ops.Dataset.from_tensors(rt).repeat(10).padded_batch(10)
