# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
with ops.Graph().as_default() as expected_graph:
    expected = array_ops.placeholder(dtypes.float32, 1, name="right")
    tensor_info = utils.build_tensor_info(expected)
with ops.Graph().as_default():  # Some other graph.
    array_ops.placeholder(dtypes.float32, 1, name="other")
actual = utils.get_tensor_from_tensor_info(tensor_info,
                                           graph=expected_graph)
self.assertIsInstance(actual, ops.Tensor)
self.assertIs(actual.graph, expected_graph)
self.assertEqual(expected.name, actual.name)
