# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
params = StructuredTensor.from_pyval(params)
# Shouldn't need to do this, but see cl/366396997
indices = ragged_factory_ops.constant(indices)
# validate_indices isn't actually used, and we aren't testing names
actual = array_ops.gather(
    params,
    indices,
    validate_indices=True,
    axis=axis,
    name=None,
    batch_dims=batch_dims)
self.assertAllEqual(actual, expected)
