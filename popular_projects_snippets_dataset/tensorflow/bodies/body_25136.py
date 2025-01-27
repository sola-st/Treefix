# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
self._tmp_dir = tempfile.mkdtemp()
self._tmp_config_path = os.path.join(self._tmp_dir, ".tfdbg_config")
self.assertFalse(gfile.Exists(self._tmp_config_path))
super(CLIConfigTest, self).setUp()
