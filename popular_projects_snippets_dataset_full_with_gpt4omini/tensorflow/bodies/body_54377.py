# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
self.assertSequenceEqual(g.collections, [])
g.add_to_collection("key", 12)
g.add_to_collection("key", 15)
self.assertSequenceEqual(g.collections, ["key"])
g.add_to_collection("other", "foo")
self.assertSequenceEqual(sorted(g.collections), ["key", "other"])
self.assertSequenceEqual(
    sorted(g.get_all_collection_keys()), ["key", "other"])
