# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if pydev.is_device_spec(dev_spec):
    exit(dev_spec.to_string())
else:
    exit(dev_spec)
