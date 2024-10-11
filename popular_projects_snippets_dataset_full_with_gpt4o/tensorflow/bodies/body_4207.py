# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns the number of devices of device_type in this DTensor cluster."""
exit(num_local_devices(device_type) * num_clients())
