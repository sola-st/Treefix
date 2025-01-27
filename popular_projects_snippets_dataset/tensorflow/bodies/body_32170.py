# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
# Prepare the input tensor.
if input_is_ragged:
    input = ragged_factory_ops.constant(input, dtype=dtypes.string)
else:
    input = constant_op.constant(input, dtype=dtypes.string)

expected_ragged = ragged_factory_ops.constant(expected)
actual_ragged_v1 = ragged_string_ops.strings_split_v1(
    input, result_type="RaggedTensor", **kwargs)
actual_ragged_v1_input_kwarg = ragged_string_ops.strings_split_v1(
    input=input, result_type="RaggedTensor", **kwargs)
actual_ragged_v1_source_kwarg = ragged_string_ops.strings_split_v1(
    source=input, result_type="RaggedTensor", **kwargs)
self.assertAllEqual(expected_ragged, actual_ragged_v1)
self.assertAllEqual(expected_ragged, actual_ragged_v1_input_kwarg)
self.assertAllEqual(expected_ragged, actual_ragged_v1_source_kwarg)
expected_sparse = self.evaluate(expected_ragged.to_sparse())
actual_sparse_v1 = ragged_string_ops.strings_split_v1(
    input, result_type="SparseTensor", **kwargs)
self.assertEqual(expected_sparse.indices.tolist(),
                 self.evaluate(actual_sparse_v1.indices).tolist())
self.assertEqual(expected_sparse.values.tolist(),
                 self.evaluate(actual_sparse_v1.values).tolist())
self.assertEqual(expected_sparse.dense_shape.tolist(),
                 self.evaluate(actual_sparse_v1.dense_shape).tolist())
