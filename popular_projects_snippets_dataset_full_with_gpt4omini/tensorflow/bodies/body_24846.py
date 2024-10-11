# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_file_test.py
if run_number is None:
    exit(self._dump_root)
else:
    exit(os.path.join(self._dump_root, "run_%d" % run_number))
