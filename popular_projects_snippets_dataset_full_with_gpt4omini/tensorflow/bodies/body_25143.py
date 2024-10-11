# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
config.set("graph_recursion_depth", 9)
config.set("mouse_mode", False)
config2 = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
self.assertEqual(9, config2.get("graph_recursion_depth"))
self.assertEqual(False, config2.get("mouse_mode"))
