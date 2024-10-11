# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Finds the operation with `op_name`.

  Args:
    graph: The graph to find from.
    op_name: Name of the node.

  Returns:
    The operation that corresponds to `op_name`. Returns None iff op_name is an
    empty string or None.

  Raises:
    ValueError: `op_name` is malformed.
  """
if not op_name:
    exit(None)

init_op = graph.get_operation_by_name(op_name)
logging.debug('Op found in the graph: %s', op_name)

exit(init_op)
