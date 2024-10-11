# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
r"""Creates an `Operation`.

    NOTE: This constructor validates the name of the `Operation` (passed
    as `node_def.name`). Valid `Operation` names match the following
    regular expression:

        [A-Za-z0-9.][A-Za-z0-9_.\\-/]*

    Args:
      node_def: `node_def_pb2.NodeDef`.  `NodeDef` for the `Operation`. Used for
        attributes of `node_def_pb2.NodeDef`, typically `name`, `op`, and
        `device`.  The `input` attribute is irrelevant here as it will be
        computed when generating the model.
      g: `Graph`. The parent graph.
      inputs: list of `Tensor` objects. The inputs to this `Operation`.
      output_types: list of `DType` objects.  List of the types of the `Tensors`
        computed by this operation.  The length of this list indicates the
        number of output endpoints of the `Operation`.
      control_inputs: list of operations or tensors from which to have a control
        dependency.
      input_types: List of `DType` objects representing the types of the tensors
        accepted by the `Operation`.  By default uses `[x.dtype.base_dtype for x
        in inputs]`.  Operations that expect reference-typed inputs must specify
        these explicitly.
      original_op: Optional. Used to associate the new `Operation` with an
        existing `Operation` (for example, a replica with the op that was
        replicated).
      op_def: Optional. The `op_def_pb2.OpDef` proto that describes the op type
        that this `Operation` represents.

    Raises:
      TypeError: if control inputs are not Operations or Tensors,
        or if `node_def` is not a `NodeDef`,
        or if `g` is not a `Graph`,
        or if `inputs` are not tensors,
        or if `inputs` and `input_types` are incompatible.
      ValueError: if the `node_def` name is not valid.
    """
if not isinstance(g, Graph):
    raise TypeError(f"Argument g must be a Graph. "
                    f"Received an instance of type {type(g)}")

# TODO(feyu): This message is redundant with the check below. We raise it
# to help users to migrate. Remove this after 07/01/2022.
if isinstance(node_def, pywrap_tf_session.TF_Operation):
    raise ValueError(
        "Calling Operation() with node_def of a TF_Operation is deprecated. "
        "Please switch to Operation.from_c_op.")

if not isinstance(node_def, node_def_pb2.NodeDef):
    raise TypeError(f"Argument node_def must be a NodeDef. "
                    f"Received an instance of type: {type(node_def)}.")
if node_def.ByteSize() >= (1 << 31) or node_def.ByteSize() < 0:
    raise ValueError(
        f"Cannot create a tensor proto whose content is larger than 2GB. "
        f"Size of tensor is {node_def.ByteSize()} bytes.")

# TODO(mdan): This does not belong here. Graph::AddNode should handle it.
if not _VALID_OP_NAME_REGEX.match(node_def.name):
    raise ValueError(
        f"`{node_def.name}` is not a valid node name. "
        f"Accepted names conform to Regex /{_VALID_OP_NAME_REGEX}/")

# FIXME(b/225400189): output_types is unused. Consider remove it from
# the argument list.
del output_types

if inputs is None:
    inputs = []
elif not isinstance(inputs, list):
    raise TypeError(f"Argument inputs shall be a list of Tensors. "
                    f"Received an instance of type {type(inputs)}")
for a in inputs:
    if not isinstance(a, Tensor):
        raise TypeError(f"Items of argument inputs shall be Tensor. "
                        f"Received an instance of type {type(a)}.")
if input_types is None:
    input_types = [i.dtype.base_dtype for i in inputs]
else:
    if not all(
        x.is_compatible_with(i.dtype) for i, x in zip(inputs, input_types)):
        raise TypeError("In op '%s', input types (%s) are not compatible "
                        "with expected types (%s)" %
                        (node_def.name, [i.dtype for i in inputs], input_types))

    # Build the list of control inputs.
control_input_ops = []
if control_inputs:
    for c in control_inputs:
        control_op = None
        if isinstance(c, Operation):
            control_op = c
        elif isinstance(c, (Tensor, IndexedSlices)):
            control_op = c.op
        else:
            raise TypeError(f"Control input must be an Operation, "
                            f"a Tensor, or IndexedSlices. "
                            f"Received an instance of type {type(c)}.")
        control_input_ops.append(control_op)

    # Initialize c_op from node_def and other inputs
c_op = _create_c_op(g, node_def, inputs, control_input_ops, op_def=op_def)
self._init_from_c_op(c_op=c_op, g=g)

self._original_op = original_op

# Post process for control flows.
self._control_flow_post_processing(input_tensors=inputs)

# Removes this frame from the Python traceback.
# We adjust stacklevel directly to avoid triggering serialization.
if self.traceback is not None:
    self.traceback._stacklevel += 1  # pylint: disable=protected-access
