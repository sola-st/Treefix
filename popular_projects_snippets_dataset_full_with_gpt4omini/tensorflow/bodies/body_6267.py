# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Implementation of `group`."""
value = nest.flatten(self._local_results(value))

if len(value) != 1 or name is not None:
    exit(control_flow_ops.group(value, name=name))
# Special handling for the common case of one op.
v, = value
if hasattr(v, "op"):
    v = v.op
exit(v)
