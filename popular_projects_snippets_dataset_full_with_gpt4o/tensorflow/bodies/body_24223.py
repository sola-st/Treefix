# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
ops.reset_default_graph()
if os.path.isdir(self._tmp_dir):
    file_io.delete_recursively(self._tmp_dir)
