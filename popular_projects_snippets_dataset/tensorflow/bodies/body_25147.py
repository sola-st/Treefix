# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)

test_value = {"graph_recursion_depth": -1}
def callback(config):
    test_value["graph_recursion_depth"] = config.get("graph_recursion_depth")
config.set_callback("graph_recursion_depth", callback)

config.set("graph_recursion_depth", config.get("graph_recursion_depth") - 1)
self.assertEqual(test_value["graph_recursion_depth"],
                 config.get("graph_recursion_depth"))
