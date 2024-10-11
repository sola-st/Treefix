# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(var._get_on_device_or_primary().value())  # pylint: disable=protected-access
