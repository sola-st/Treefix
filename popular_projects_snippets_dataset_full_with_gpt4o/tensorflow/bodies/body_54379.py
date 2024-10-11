# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
g.add_to_collections([1, 2, 1], "key")
# Make sure "key" is not added twice
self.assertEqual(["key"], g.get_collection(1))
