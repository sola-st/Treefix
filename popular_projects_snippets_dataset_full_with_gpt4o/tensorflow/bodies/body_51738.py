# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
expected = array_ops.sparse_placeholder(dtypes.float32, name="x")
tensor_info = utils.build_tensor_info(expected)
actual = utils.get_tensor_from_tensor_info(tensor_info)
self.assertIsInstance(actual, sparse_tensor.SparseTensor)
self.assertEqual(expected.values.name, actual.values.name)
self.assertEqual(expected.indices.name, actual.indices.name)
self.assertEqual(expected.dense_shape.name, actual.dense_shape.name)
