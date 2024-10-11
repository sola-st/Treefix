# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
params = StructuredTensor.from_pyval(params)
with self.assertRaisesRegex(error_type, error_regex):
    structured_array_ops.gather(
        params,
        indices,
        validate_indices=True,
        axis=axis,
        name=None,
        batch_dims=batch_dims)
