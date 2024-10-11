# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
input_tensor = np.array(_nested_encode(texts, "UTF-8"), dtype=bytes)
result = ragged_string_ops.unicode_split(input_tensor, "UTF-8").to_sparse()
self.assertIsInstance(result, sparse_tensor.SparseTensor)
self.assertAllEqual(expected.indices, result.indices)
self.assertAllEqual(expected.values, result.values)
self.assertAllEqual(expected.dense_shape, result.dense_shape)
