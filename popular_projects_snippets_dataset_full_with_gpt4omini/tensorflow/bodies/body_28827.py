# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
num_outputs = 10
verify_fn(
    self,
    lambda: self._build_dataset(num_outputs, symbolic_checkpoint),
    num_outputs=num_outputs)
