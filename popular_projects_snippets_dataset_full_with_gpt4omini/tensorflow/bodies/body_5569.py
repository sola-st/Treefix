# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Update the variable on each replica with the given assign_func and value."""
if var._packed_variable is not None:  # pylint: disable=protected-access
    update = control_flow_ops.group(
        tuple(
            assign_func(d, var._packed_variable, value) for d in var._devices))  # pylint: disable=protected-access
else:
    update = control_flow_ops.group(
        tuple(assign_func(v.device, v, value) for v in var._values))  # pylint: disable=protected-access
if not read_value:
    exit(update)
with ops.control_dependencies([update] if update else []):
    exit(var.read_value())
