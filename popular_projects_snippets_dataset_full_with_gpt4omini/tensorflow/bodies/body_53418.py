# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Creates a TF_Operation.

  Args:
    graph: a `Graph`.
    node_def: `node_def_pb2.NodeDef` for the operation to create.
    inputs: A flattened list of `Tensor`s. This function handles grouping
      tensors into lists as per attributes in the `node_def`.
    control_inputs: A list of `Operation`s to set as control dependencies.
    op_def: Optional. `op_def_pb2.OpDef` for the operation to create. If not
      specified, is looked up from the `graph` using `node_def.op`.
    extract_traceback: if True, extract the current Python traceback to the
      TF_Operation.

  Returns:
    A wrapped TF_Operation*.
  """
if op_def is None:
    op_def = graph._get_op_def(node_def.op)  # pylint: disable=protected-access
# TODO(skyewm): op_def_library.apply_op() flattens the incoming inputs.
# Refactor so we don't have to do this here.
inputs = _reconstruct_sequence_inputs(op_def, inputs, node_def.attr)
# pylint: disable=protected-access
with graph._c_graph.get() as c_graph:
    op_desc = pywrap_tf_session.TF_NewOperation(c_graph,
                                                compat.as_str(node_def.op),
                                                compat.as_str(node_def.name))
if node_def.device:
    pywrap_tf_session.TF_SetDevice(op_desc, compat.as_str(node_def.device))
# Add inputs
for op_input in inputs:
    if isinstance(op_input, (list, tuple)):
        pywrap_tf_session.TF_AddInputList(op_desc,
                                          [t._as_tf_output() for t in op_input])
    else:
        pywrap_tf_session.TF_AddInput(op_desc, op_input._as_tf_output())

  # Add control inputs
for control_input in control_inputs:
    pywrap_tf_session.TF_AddControlInput(op_desc, control_input._c_op)
# pylint: enable=protected-access

# Add attrs
for name, attr_value in node_def.attr.items():
    serialized = attr_value.SerializeToString()
    # TODO(skyewm): this creates and deletes a new TF_Status for every attr.
    # It might be worth creating a convenient way to re-use the same status.
    pywrap_tf_session.TF_SetAttrValueProto(op_desc, compat.as_str(name),
                                           serialized)

try:
    c_op = pywrap_tf_session.TF_FinishOperation(op_desc)
except errors.InvalidArgumentError as e:
    # Convert to ValueError for backwards compatibility.
    raise ValueError(e.message)

# Record the current Python stack trace as the creating stacktrace of this
# TF_Operation.
if extract_traceback:
    tf_stack.extract_stack_for_op(c_op, stacklevel=3)

exit(c_op)
