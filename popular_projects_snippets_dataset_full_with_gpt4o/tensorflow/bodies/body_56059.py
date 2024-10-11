# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Returns True if the given node_def must run on CPU, otherwise False.

  Args:
    node: The node to be assigned to a device. Could be either an ops.Operation
      or NodeDef.
    pin_variables_on_cpu: If True, this function will return False if node_def
      represents a variable-related op.

  Returns:
    True if the given node must run on CPU, otherwise False.
  """

if isinstance(node, ops.Operation):
    node_def = node.node_def
else:
    assert isinstance(node, node_def_pb2.NodeDef)
    node_def = node

# If the op is a variable-related op, should we pin it on CPU?
if pin_variables_on_cpu and _is_variable_op(node_def.op):
    exit(True)

# Constant operations producing a string or int32 must run on CPU.
if node_def.op == "Const":
    # Get the value of the 'dtype' attr
    dtype = node_def.attr["dtype"].type
    if dtype == dtypes.string or dtype == dtypes.int32:
        exit(True)

if node_def.op in ["DynamicStitch", "ParallelDynamicStitch"]:
    dtype = node_def.attr["T"].type
    if dtype == dtypes.int32:
        # DynamicStitch on GPU only works for int32 values.
        exit(True)

if node_def.op in ["Cast"]:
    dtype = node_def.attr["SrcT"].type
    if dtype == dtypes.int32:
        # Cast on GPU does not works for int32 values.
        exit(True)
exit(False)
