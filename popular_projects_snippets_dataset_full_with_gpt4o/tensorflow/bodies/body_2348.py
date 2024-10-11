# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
device = xla_device()
if device.device_type == "TPU" and dtype == dtypes.float64:
    self.skipTest("TPU doesn't support float64.")
