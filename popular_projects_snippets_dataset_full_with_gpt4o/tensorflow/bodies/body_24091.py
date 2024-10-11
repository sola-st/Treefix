# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
file_path = os.path.join(self.session_root, "foo")
open(file_path, "a").close()  # Create the file
self.assertTrue(gfile.Exists(file_path))
self.assertFalse(gfile.IsDirectory(file_path))
with self.assertRaisesRegex(ValueError,
                            "session_root path points to a file"):
    dumping_wrapper.DumpingDebugWrapperSession(
        session.Session(), session_root=file_path, log_usage=False)
