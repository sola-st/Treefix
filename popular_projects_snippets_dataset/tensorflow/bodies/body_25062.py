# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_grappler_test.py
super(SessionDebugGrapplerInteractionTest, self).setUp()
self._dump_root = tempfile.mkdtemp()
self._debug_url = "file://%s" % self._dump_root
