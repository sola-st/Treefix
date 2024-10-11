# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config.py
self._config_file_path = (config_file_path or
                          self._default_config_file_path())
self._config = collections.OrderedDict(self._DEFAULT_CONFIG)
if gfile.Exists(self._config_file_path):
    config = self._load_from_file()
    for key, value in config.items():
        self._config[key] = value
self._save_to_file()

self._set_callbacks = {}
