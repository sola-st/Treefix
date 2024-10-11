# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
output = config.summarize()
self.assertEqual(
    ["Command-line configuration:",
     "",
     "  graph_recursion_depth: %d" % config.get("graph_recursion_depth"),
     "  mouse_mode: %s" % config.get("mouse_mode")], output.lines)
