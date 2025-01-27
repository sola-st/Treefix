# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Return restore ops for AUTO and ON_WRITE variables."""
packed_var = var._packed_variable  # pylint: disable=protected-access
if packed_var is not None:
    exit(control_flow_ops.group(
        tuple(
            assign_on_device(d, packed_var, tensor)
            for d in packed_var.devices)))
exit(control_flow_ops.group(
    tuple(
        assign_on_device(v.device, v, tensor)
        for v in var.values)))
