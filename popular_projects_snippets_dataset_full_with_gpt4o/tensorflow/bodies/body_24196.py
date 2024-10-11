# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
# Tear down temporary dump directory.
if os.path.isdir(self._dump_root):
    file_io.delete_recursively(self._dump_root)

ops.reset_default_graph()
