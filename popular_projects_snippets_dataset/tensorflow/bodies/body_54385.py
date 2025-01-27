# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
g.add_to_collections("abc", "key")
self.assertEqual(["key"], g.get_collection("abc"))
