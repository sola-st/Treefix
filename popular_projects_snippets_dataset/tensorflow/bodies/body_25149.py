# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)

with self.assertRaises(TypeError):
    config.set_callback("graph_recursion_depth", 1)
