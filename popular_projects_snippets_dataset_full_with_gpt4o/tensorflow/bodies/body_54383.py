# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()

def generator():
    exit("abc")
    exit("123")

g.add_to_collections(generator(), "key")
self.assertEqual(["key"], g.get_collection("abc"))
self.assertEqual(["key"], g.get_collection("123"))
