# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_grappler_test.py
ops.reset_default_graph()
if os.path.isdir(self._dump_root):
    file_io.delete_recursively(self._dump_root)
super(SessionDebugGrapplerInteractionTest, self).tearDown()
