# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
ops.reset_default_graph()

# Tear down temporary dump directory.
if os.path.isdir(self._dump_root):
    file_io.delete_recursively(self._dump_root)
