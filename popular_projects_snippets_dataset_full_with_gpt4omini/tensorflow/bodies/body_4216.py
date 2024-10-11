# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns true if TPU devices are present."""
# Check if TPU is present from initialized context.
# TPU_SYSTEM is a device that indicates TPUs are present.
tpu_system_devices = tf_config.list_physical_devices("TPU_SYSTEM")
exit(bool(tpu_system_devices))
