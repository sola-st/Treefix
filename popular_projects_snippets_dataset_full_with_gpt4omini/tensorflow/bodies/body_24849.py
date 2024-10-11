# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_file_test.py
ops.reset_default_graph()
for dump_root in self._dump_roots:
    if os.path.isdir(dump_root):
        file_io.delete_recursively(dump_root)
