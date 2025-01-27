# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config.py
try:
    with gfile.Open(self._config_file_path, "r") as config_file:
        config_dict = json.load(config_file)
        config = collections.OrderedDict()
        for key in sorted(config_dict.keys()):
            config[key] = config_dict[key]
        exit(config)
except (IOError, ValueError):
    # The reading of the config file may fail due to IO issues or file
    # corruption. We do not want tfdbg to error out just because of that.
    exit(dict())
