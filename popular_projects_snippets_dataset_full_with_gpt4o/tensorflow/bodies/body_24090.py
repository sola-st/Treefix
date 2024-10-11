# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
dir_path = os.path.join(self.session_root, "foo")
os.mkdir(dir_path)
self.assertTrue(os.path.isdir(dir_path))

with self.assertRaisesRegex(
    ValueError, "session_root path points to a non-empty directory"):
    dumping_wrapper.DumpingDebugWrapperSession(
        session.Session(), session_root=self.session_root, log_usage=False)
