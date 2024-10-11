# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
if os.path.isdir(self.dump_root):
    file_io.delete_recursively(self.dump_root)
ops.reset_default_graph()
