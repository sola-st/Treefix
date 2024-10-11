# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
expected = array_ops.placeholder(dtypes.float32, 1, name="x")
tensor_info = utils.build_tensor_info(expected)
actual = utils.get_tensor_from_tensor_info(tensor_info)
self.assertIsInstance(actual, ops.Tensor)
self.assertEqual(expected.name, actual.name)
