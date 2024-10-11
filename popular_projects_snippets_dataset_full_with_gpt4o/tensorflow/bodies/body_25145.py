# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
output = config.summarize(highlight="mouse_mode")
self.assertEqual(
    ["Command-line configuration:",
     "",
     "  graph_recursion_depth: %d" % config.get("graph_recursion_depth"),
     "  mouse_mode: %s" % config.get("mouse_mode")], output.lines)
self.assertEqual((2, 12, ["underline", "bold"]),
                 output.font_attr_segs[3][0])
self.assertEqual((14, 18, "bold"), output.font_attr_segs[3][1])
