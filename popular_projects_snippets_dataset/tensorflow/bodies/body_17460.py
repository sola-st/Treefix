# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if context.executing_eagerly():
    exit(self.read_value().numpy())
raise NotImplementedError(
    "numpy() is only available when eager execution is enabled.")
