# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

tensor = constant_op.constant([1])
self.assertEqual(
    inspect_utils.getmethodclass(tensor.get_shape), type(tensor))
