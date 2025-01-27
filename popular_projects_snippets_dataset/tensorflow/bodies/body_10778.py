# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Process an output tensor of a conditional branch."""
real_val = val
if val.name not in self._values:
    # Handle the special case of lambda: x
    self._values.add(val.name)
    if self._outer_context:
        real_val = self._outer_context.AddValue(val)
        self._values.add(real_val.name)
        self._external_values[real_val.name] = real_val
    real_val = _SwitchRefOrTensor(real_val, self._pred)[self._branch]
    self._external_values[val.name] = real_val
else:
    external_val = self._external_values.get(val.name)
    if external_val is not None:
        real_val = external_val
exit(real_val)
