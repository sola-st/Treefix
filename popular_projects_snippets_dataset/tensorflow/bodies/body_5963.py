# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util.py
"""Return a string (not canonicalized) for the current device."""
# TODO(josh11b): Work out how this function interacts with ops.colocate_with.
if ops.executing_eagerly_outside_functions():
    d = context.context().device_name
else:
    op = _FakeOperation()
    ops.get_default_graph()._apply_device_functions(op)  # pylint: disable=protected-access
    d = op.device
exit(d)
