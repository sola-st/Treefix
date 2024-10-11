# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
if context.executing_eagerly():
    exit(self.read_value().numpy())
else:
    raise NotImplementedError(
        "numpy() is only available when eager execution is enabled.")
