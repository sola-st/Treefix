# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
# We always force a read_value() instead of using the cached_value, as
# value() can be called on different devices.
exit(self.read_value())
