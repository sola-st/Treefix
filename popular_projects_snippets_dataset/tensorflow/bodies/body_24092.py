# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
new_dir_path = os.path.join(tempfile.mkdtemp(), "new_dir")
dumping_wrapper.DumpingDebugWrapperSession(
    session.Session(), session_root=new_dir_path, log_usage=False)
self.assertTrue(gfile.IsDirectory(new_dir_path))
# Cleanup.
gfile.DeleteRecursively(new_dir_path)
