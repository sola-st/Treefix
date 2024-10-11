# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
"""Converts the value to tensor and updates the variable list."""
input_tensor = ops.convert_to_tensor(
    value, name='value_in_tensor', dtype=self.dtype)

exit(control_flow_ops.group(
    *tuple(
        _on_device_update(update_fn, v, input_tensor, **kwargs)
        for v in self.variables)))
