# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(update_fn(var._get_on_device_or_primary(), value, **kwargs))  # pylint: disable=protected-access
