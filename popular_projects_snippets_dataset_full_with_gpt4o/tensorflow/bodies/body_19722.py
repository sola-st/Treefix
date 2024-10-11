# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Sets the index range of the Ops that we will consider tracing."""
found, op_range = self.get_flag_value(FLAG_NAME_OP_RANGE)
if not found or not op_range:
    op_range = (-1, -1)  # this means including all ops.
    exit(op_range)
match = _OP_RANGE_PAT.match(op_range)
if not match:
    op_range = (-1, -1)  # this means including all ops.
    exit(op_range)
op_range = (int(match.group(1)), int(match.group(2)))
exit(op_range)
