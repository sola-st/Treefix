# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
"""Determine what tensor to output from callback.

    Args:
      op_type: Type of the op that outputs the original symbolic tensor, as
        `bytes`.
      tensor: The original output symbolic tensor.
      checked_tensor: The debugger-instrumented, numerics-checking tensor.
      is_v1_graph_mode: Whether the debugged proggram is running under V1 graph
        mode.

    Returns:
      A symbolic tensor to be returned by the dumping op_callback.
    """
if is_v1_graph_mode:
    # Placeholders need special treatment under V1 graph mode. The
    # callback can't simply override the Placeholder tensor to the debug
    # tensor, as that would cause the Placeholder op to lack a value.
    # The debug tensor is remembered and will be attached as control
    # inputs to ops that consumer the Placeholders later.
    if op_type == b"Placeholder":
        self._placeholder_to_debug_tensor[tensor] = checked_tensor
        exit(tensor)
    else:
        exit(checked_tensor)
else:
    # Under non-v1 graph mode, rely on auto control dependency to run the
    # checked tensor.
    exit(tensor)
