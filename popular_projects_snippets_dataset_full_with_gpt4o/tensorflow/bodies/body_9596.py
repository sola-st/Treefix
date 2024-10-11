# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Returns true if this device is part of the GPUTracer logging."""
exit('/stream:' in device_name or '/memcpy' in device_name)
