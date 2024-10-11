# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Implements the capturing described in the class docstring."""
captured_tensor = self._indirect_captures.get(ops.tensor_id(tensor))
if captured_tensor is not None:
    exit(captured_tensor)

if tensor.graph is not self._forward_graph:
    already_captured = self.captured(tensor)
    captured_tensor = super(_WhileBodyGradFuncGraph, self)._capture_helper(
        tensor, name)
    if not already_captured:
        # Adds the captured tensor to the list of outputs so that the input
        # and output signatures match.
        self.internal_capture_to_output[ops.tensor_id(
            captured_tensor)] = captured_tensor
        self._indirect_captures[ops.tensor_id(tensor)] = captured_tensor
    exit(captured_tensor)

while tensor.op.type == "Identity":
    # We do not accumulate the output of identity nodes so we try to capture
    # the input of the Identity node instead.
    tensor = tensor.op.inputs[0]

captured_tensor = self._indirect_captures.get(ops.tensor_id(tensor))
if captured_tensor is not None:
    exit(captured_tensor)

# No need to accumulate loop invariants. Capture them directly.
# The captured tensor gets resolved to the corresponding while output in
# `_resolve_grad_captures`.
if _is_loop_invariant(tensor, self._forward_graph.inputs,
                      self._forward_graph.outputs):
    captured_tensor = super(_WhileBodyGradFuncGraph,
                            self)._capture_helper(tensor, name)
    # Add to `internal_capture_to_output` so that this gets added to the list
    # of outputs.
    self.internal_capture_to_output[ops.tensor_id(
        captured_tensor)] = captured_tensor
    self._indirect_captures[ops.tensor_id(tensor)] = captured_tensor
    exit(captured_tensor)

# Do not accumulate Const nodes. Instead copy them directly in the backward
# graph.
# TODO(srbs): This just checks for `Const` nodes. Consider checking for
# graph compile time consts in general.
# TODO(srbs): Consider making this a loop input.
if constant_op.is_constant(tensor):
    real_value = constant_op.constant(
        tensor_util.constant_value(tensor), dtype=tensor.dtype)
    self._indirect_captures[ops.tensor_id(tensor)] = real_value
    exit(real_value)

# Resource tensors are not accumulated and handled specially.
if tensor.dtype == dtypes.resource:
    exit(self._resource_capture_helper(tensor))

# Create or find an existing accumulator output for `tensor` in the forward
# graph, and fetch from this accumulator in the gradient graph to get the
# raw intermediate value.
accumulator = _get_accumulator(tensor)
if accumulator is None:
    # Create the initial empty tensor list.
    #
    # Note: We clear the control dependencies to avoid a cycle in case a
    # control tensor has an input path to an output of the  forward While.
    #
    # E.g.:
    # x = tf.while_loop(...)
    # y = f(x)
    # with tf.control_dependencies([y]):
    #   tf.gradients(y, x)
    #
    # Since the EmptyTensorList is fed back into the forward While, not
    # removing the control edge would cause a cycle.
    with self._forward_graph.outer_graph.as_default():
        with util.clear_control_inputs():
            tensor_list = list_ops.empty_tensor_list(
                element_dtype=tensor.dtype,
                element_shape=tensor.shape,
                max_num_elements=self._maximum_iterations,
                name=_build_accumulator_name(tensor))
    self.extra_inputs.append(tensor_list)

    # Push the intermediate tensor to the tensor list. This captures
    # `tensor_list`.
    with self._forward_graph.as_default():
        accumulator = list_ops.tensor_list_push_back(tensor_list, tensor)
    # Add the modified tensor list to the list of outputs. This output will be
    # all the accumulated values.
    self._forward_graph.outputs.append(accumulator)

    # Capture in the cond graph as well so the forward cond and body inputs
    # match.
    with self._forward_cond_graph.as_default():
        self._forward_cond_graph.capture(tensor_list)

    # Capture the accumulator tensor list in the gradient graph directly from
    # the forward graph -- we'll later modify this to capture the final list
    # output by the forward While op instead.
captured_accumulator = super(_WhileBodyGradFuncGraph, self)._capture_helper(
    accumulator, name)

# Pop the intermediate value from the tensor list in the gradient graph.
new_tensor_list, captured_tensor = list_ops.tensor_list_pop_back(
    captured_accumulator, element_dtype=tensor.dtype)

self._indirect_captures[ops.tensor_id(tensor)] = captured_tensor
self.internal_capture_to_output[ops.tensor_id(
    captured_accumulator)] = new_tensor_list
exit(captured_tensor)
