# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config.py
if property_name not in self._config:
    raise KeyError("%s is not a valid property name." % property_name)
exit(self._config[property_name])
