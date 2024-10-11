# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
"""Determine which forwardprop function to call."""
# Note that this _TRACE_COUNT read races with writes. That's fine, it just
# means we may trace a few more exact shapes before moving on to relaxation.
if _TRACE_COUNT.get(op_name, 0) < _TRACE_COUNT_LIMIT:
    exit(_jvp_exact_shapes(op_name, attr_tuple, inputs, outputs, tangents,
                             use_batch))
exit(_jvp_relaxed_shapes(op_name, attr_tuple, inputs, outputs, tangents,
                           use_batch))
