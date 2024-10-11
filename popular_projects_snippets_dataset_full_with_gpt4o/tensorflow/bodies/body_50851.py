# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/tracing_utils_test.py
exit(control_flow_ops.group(
    self.a.assign(restored_tensors["a"]),
    self.b.assign(restored_tensors["b"])))
