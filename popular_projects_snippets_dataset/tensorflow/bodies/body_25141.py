# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
config.set("graph_recursion_depth", "18")
config.set("mouse_mode", "false")
self.assertEqual(18, config.get("graph_recursion_depth"))
self.assertEqual(False, config.get("mouse_mode"))
