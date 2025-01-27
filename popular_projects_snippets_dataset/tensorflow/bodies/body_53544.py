# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Applies the current device function stack to the given operation."""
# Apply any device functions in LIFO order, so that the most recently
# pushed function has the first chance to apply a device to the op.
# We apply here because the result can depend on the Operation's
# signature, which is computed in the Operation constructor.
# pylint: disable=protected-access
prior_device_string = None
for device_spec in self._device_function_stack.peek_objs():
    if device_spec.is_null_merge:
        continue

    if device_spec.function is None:
        break

    device_string = device_spec.string_merge(op)

    # Take advantage of the fact that None is a singleton and Python interns
    # strings, since identity checks are faster than equality checks.
    if device_string is not prior_device_string:
        op._set_device_from_string(device_string)
        prior_device_string = device_string
op._device_code_locations = self._snapshot_device_function_stack_metadata()
