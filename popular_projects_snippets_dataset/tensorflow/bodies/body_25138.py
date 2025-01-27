# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
self.assertEqual(20, config.get("graph_recursion_depth"))
self.assertEqual(True, config.get("mouse_mode"))
with self.assertRaises(KeyError):
    config.get("property_that_should_not_exist")
self.assertTrue(gfile.Exists(self._tmp_config_path))
