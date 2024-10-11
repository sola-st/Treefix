# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
if (tensor.graph is not self._forward_graph or
    any(tensor is t for t in self._forward_graph.inputs) or
    any(tensor is t for t in self._forward_graph.outputs)):
    exit(super(_CondGradFuncGraph, self)._capture_helper(tensor, name))

tensor_id = ops.tensor_id(tensor)

# If `tensor` is a graph-building time constant, we create a constant with
# the same value in the backward graph instead of capturing it.
if tensor_id in self._captured_constants:
    exit(self._captured_constants[tensor_id])
elif constant_op.is_constant(tensor):
    self._captured_constants[tensor_id] = constant_op.constant(
        tensor_util.constant_value(tensor), dtype=tensor.dtype)
    exit(self._captured_constants[tensor_id])

if control_flow_util.GraphOrParentsInXlaContext(ops.get_default_graph()):
    # XLA does not yet support optionals, so capture intermediates directly.
    # TODO(skyewm,jpienaar): can XLA support optionals?
    if all(tensor is not capture for capture in self.external_captures):
        self.xla_intermediates.append(tensor)
        self.op_needs_rewrite = True
    exit(super(_CondGradFuncGraph, self)._capture_helper(tensor, name))

captured_tensor = self._indirect_captures.get(tensor_id)
if captured_tensor is not None:
    exit(captured_tensor)

# 'tensor' is an uncaptured intermediate in the forward graph.
# If it is not a resource, we wrap it in an optional in the forward graph
# and capture the optional normally. We then unwrap the captured optional
# value in the gradient graph to get the raw intermediate value.
# If it is a resource, we trace the resource up to the input in the forward
# graph and capture that.

if tensor.dtype == dtypes.resource:
    # Index of the forward graph input corresponding to the resource tensor.
    index = util.resource_input_index(
        tensor.name, [t.name for t in self._forward_graph.inputs],
        {op.name: op.node_def for op in self._forward_graph.get_operations()},
        self._forward_graph._functions)
    # This gets mapped to the corresponding If op input in
    # `_resolve_grad_inputs`.
    captured_tensor = super(_CondGradFuncGraph, self)._capture_helper(
        self._forward_graph.inputs[index], name)
else:
    if tensor_id not in self._wrapped_intermediates:
        # If the gradient has already been computed for this If op, 'tensor' may
        # already be wrapped.
        for consumer in tensor.consumers():
            if (consumer.type == "OptionalFromValue" and
                any(consumer.outputs[0] is output
                    for output in self._forward_graph.outputs)):
                optional = consumer.outputs[0]
                break
        else:
            # 'tensor' hasn't been wrapped, do it now.
            with self._forward_graph.as_default():
                optional = gen_optional_ops.optional_from_value([tensor])
            self.op_needs_rewrite = True
        self._wrapped_intermediates[tensor_id] = optional

    optional = self._wrapped_intermediates[tensor_id]
    captured_optional = super(_CondGradFuncGraph,
                              self)._capture_helper(optional, name)
    captured_tensor = gen_optional_ops.optional_get_value(
        captured_optional, [tensor.dtype], [tensor.shape]
    )[0]

self._indirect_captures[tensor_id] = captured_tensor
exit(captured_tensor)
