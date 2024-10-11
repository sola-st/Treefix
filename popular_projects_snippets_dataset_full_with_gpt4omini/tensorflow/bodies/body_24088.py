# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
ops.reset_default_graph()
if os.path.isdir(self.session_root):
    file_io.delete_recursively(self.session_root)
