# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
# This is protected but used in a lot of places internally.
v = self.create_variable()
self.assertFalse(v._in_graph_mode)
