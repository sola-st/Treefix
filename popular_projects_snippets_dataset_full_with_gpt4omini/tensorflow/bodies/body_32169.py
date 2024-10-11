# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
# Check that we are matching the behavior of Python's str.split:
self.assertEqual(expected, self._py_split(input, **kwargs))

# Prepare the input tensor.
if input_is_ragged:
    input = ragged_factory_ops.constant(input, dtype=dtypes.string)
else:
    input = constant_op.constant(input, dtype=dtypes.string)

# Check that the public version (which returns a RaggedTensor) works
# correctly.
expected_ragged = ragged_factory_ops.constant(
    expected, ragged_rank=input.shape.ndims)
actual_ragged_v2 = ragged_string_ops.string_split_v2(input, **kwargs)
actual_ragged_v2_input_kwarg = ragged_string_ops.string_split_v2(
    input=input, **kwargs)
self.assertAllEqual(expected_ragged, actual_ragged_v2)
self.assertAllEqual(expected_ragged, actual_ragged_v2_input_kwarg)

# Check that the internal version (which returns a SparseTensor) works
# correctly.  Note: the internal version oly supports vector inputs.
if input.shape.ndims == 1:
    expected_sparse = self.evaluate(expected_ragged.to_sparse())
    actual_sparse_v2 = string_ops.string_split_v2(input, **kwargs)
    self.assertEqual(expected_sparse.indices.tolist(),
                     self.evaluate(actual_sparse_v2.indices).tolist())
    self.assertEqual(expected_sparse.values.tolist(),
                     self.evaluate(actual_sparse_v2.values).tolist())
    self.assertEqual(expected_sparse.dense_shape.tolist(),
                     self.evaluate(actual_sparse_v2.dense_shape).tolist())
