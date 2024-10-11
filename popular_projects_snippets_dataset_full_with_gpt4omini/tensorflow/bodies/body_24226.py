# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
file_path = os.path.join(self._tmp_dir, "foo")
open(file_path, "a").close()  # Create the file
self.assertTrue(os.path.isfile(file_path))
with self.assertRaisesRegex(ValueError, "dump_root path points to a file"):
    local_cli_wrapper.LocalCLIDebugWrapperSession(
        session.Session(), dump_root=file_path, log_usage=False)
