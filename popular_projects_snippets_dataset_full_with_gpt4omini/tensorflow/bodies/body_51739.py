# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
expected = ragged_factory_ops.constant([[1, 2], [3]], name="x")
tensor_info = utils.build_tensor_info(expected)
actual = utils.get_tensor_from_tensor_info(tensor_info)
self.assertIsInstance(actual, ragged_tensor.RaggedTensor)
self.assertEqual(expected.values.name, actual.values.name)
self.assertEqual(expected.row_splits.name, actual.row_splits.name)
