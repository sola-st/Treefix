# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
exit(control_flow_ops.group(
    self.v1.assign(restored_tensors["v1"]),
    self.v2.assign(restored_tensors["v2"])))
