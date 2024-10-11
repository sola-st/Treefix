# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns true if TPU devices are present."""
exit(bool(tf_config.list_physical_devices("GPU")))
