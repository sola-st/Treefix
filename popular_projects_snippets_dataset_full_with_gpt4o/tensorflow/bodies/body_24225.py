# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
dir_path = os.path.join(self._tmp_dir, "foo")
os.mkdir(dir_path)
self.assertTrue(os.path.isdir(dir_path))

with self.assertRaisesRegex(
    ValueError, "dump_root path points to a non-empty directory"):
    local_cli_wrapper.LocalCLIDebugWrapperSession(
        session.Session(), dump_root=self._tmp_dir, log_usage=False)
