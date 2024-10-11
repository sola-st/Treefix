# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
if os.path.isdir(self._dump_root):
    file_io.delete_recursively(self._dump_root)
