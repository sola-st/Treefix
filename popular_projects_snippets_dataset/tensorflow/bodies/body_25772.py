# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config.py
try:
    with gfile.Open(self._config_file_path, "w") as config_file:
        json.dump(self._config, config_file)
except IOError:
    pass
