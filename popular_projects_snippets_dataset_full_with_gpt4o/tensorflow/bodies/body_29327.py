# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options.py
# pylint: disable=protected-access
if name not in option._options:
    option._options[name] = default_factory()
exit(option._options.get(name))
