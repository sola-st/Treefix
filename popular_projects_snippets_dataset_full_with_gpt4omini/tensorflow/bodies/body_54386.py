# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default():
    ops.add_to_collection("key", 90)
    ops.add_to_collection("key", 100)
    # Collections are ordered.
    self.assertEqual([90, 100], ops.get_collection("key"))
