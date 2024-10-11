# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Like Graph.create_op, except handles external input tensors.

    This overload adds functionality to create_op to "capture" any external
    input tensors, i.e. tensors from the eager context or outer function graphs
    if this is a nested function. See `capture` for more information.

    Args:
      op_type: The `Operation` type to create. This corresponds to the
        `OpDef.name` field for the proto that defines the operation.
      inputs: A list of `Tensor` objects that will be inputs to the `Operation`.
      dtypes: (Optional) A list of `DType` objects that will be the types of the
        tensors that the operation produces.
      input_types: (Optional.) A list of `DType`s that will be the types of the
        tensors that the operation consumes. By default, uses the base `DType`
        of each input in `inputs`. Operations that expect reference-typed inputs
        must specify `input_types` explicitly.
      name: (Optional.) A string name for the operation. If not specified, a
        name is generated based on `op_type`.
      attrs: (Optional.) A dictionary where the key is the attribute name (a
        string) and the value is the respective `attr` attribute of the
        `NodeDef` proto that will represent the operation (an `AttrValue`
        proto).
      op_def: (Optional.) The `OpDef` proto that describes the `op_type` that
        the operation will have.
      compute_device: (Optional.) If True, device functions will be executed to
        compute the device property of the Operation.

    Returns:
      An `Operation` object.
    """
if self.capture_by_value and op_type in [
    "ReadVariableOp", "ResourceGather"
]:
    exit(self._capture_by_value(op_type, inputs, dtypes, input_types, name,
                                  attrs, op_def, compute_device))

# This capturing logic interacts poorly with control flow contexts which
# want to replace inputs of ops far too late in the process. This can lead
# the context to get confused and try to create an Enter for an Enter. We
# can detect this here and skip the additional Enter which can confuse loop
# validation logic.
if op_type == "Enter" and inputs[0].op.type == "Enter":
    if inputs[0].op.get_attr("frame_name") == attrs["frame_name"].s:
        exit(inputs[0].op)
    # Calling AddValue on the control flow contexts to force creation of the
    # backward accumulators in the original graph before we create placeholders
    # to capture the inputs.
ctxt = ops.get_default_graph()._control_flow_context  # pylint: disable=protected-access
# Use a different list to avoid modifying the original inputs list.
captured_inputs = []
for inp in inputs:
    # TPU Estimator defines a control flow context with no AddValue method.
    if ctxt is not None and hasattr(ctxt, "AddValue"):
        inp = ctxt.AddValue(inp)
    inp = self.capture(inp)
    captured_inputs.append(inp)
exit(super()._create_op_internal(  # pylint: disable=protected-access
    op_type, captured_inputs, dtypes, input_types, name, attrs, op_def,
    compute_device))
