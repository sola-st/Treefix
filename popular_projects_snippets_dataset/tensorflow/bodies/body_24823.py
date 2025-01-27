# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
super(ReconstructNonDebugGraphTest, self).setUp()
self._dump_dir = tempfile.mkdtemp()
self._debug_url = "file://" + self._dump_dir
ops.reset_default_graph()
