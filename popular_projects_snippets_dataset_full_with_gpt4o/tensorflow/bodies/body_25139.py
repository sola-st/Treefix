# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
with open(self._tmp_config_path, "rt") as f:
    config_json = json.load(f)
# Remove a field to simulate forward compatibility test.
del config_json["graph_recursion_depth"]
with open(self._tmp_config_path, "wt") as f:
    json.dump(config_json, f)

config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)
self.assertEqual(20, config.get("graph_recursion_depth"))
