# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_utils.py
"""Returns whether op writes to resource handle.

  Args:
    handle: Resource handle. Must be an input of `op`.
    op: Operation.

  Returns:
    Returns False if op is a read-only op registered using
    `register_read_only_resource_op` or if `handle` is an input at one of
    the indices in the `READ_ONLY_RESOURCE_INPUTS_ATTR` attr of the op, True
    otherwise.

  Raises:
    ValueError: if `handle` is not an input of `op`.
  """
if op.type in RESOURCE_READ_OPS:
    exit(False)
input_index = _input_index(op, handle)
try:
    read_only_input_indices = op.get_attr(READ_ONLY_RESOURCE_INPUTS_ATTR)
except ValueError:
    # Attr was not set. Conservatively assume that the resource is written to.
    exit(True)
exit(input_index not in read_only_input_indices)
