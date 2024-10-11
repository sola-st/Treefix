# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Forward+backward functions where the backward function sees `outputs`."""
# First figure out which of `outputs` are trainable. We'll accept gradients
# for each of these in the backward function.
trainable_outputs = []
trainable_indices = []
for index, output in enumerate(outputs):

    if backprop_util.IsTrainable(output):
        trainable_outputs.append(output)
        trainable_indices.append(index)

backwards_graph = func_graph_module.FuncGraph(
    _backward_name(self._func_graph.name))
with backwards_graph.as_default():
    gradients_wrt_outputs = []
    for output in trainable_outputs:
        gradient_shape, gradient_dtype = default_gradient.shape_and_dtype(
            output)
        gradient_placeholder = graph_placeholder(gradient_dtype, gradient_shape)
        handle_data_util.copy_handle_data(output, gradient_placeholder)
        gradients_wrt_outputs.append(gradient_placeholder)
    with ops.device(None):
        gradients_wrt_inputs = gradients_util._GradientsHelper(  # pylint: disable=protected-access
            trainable_outputs,
            self._func_graph.inputs,
            grad_ys=gradients_wrt_outputs,
            src_graph=self._func_graph)

    if input_tangents:
        # Convert IndexedSlices to dense tensors (as we do elsewhere for
        # function gradients). Our C++ bindings don't know how to handle them
        # currently.
        gradients_wrt_inputs = nest.map_structure(
            lambda x: ops.convert_to_tensor(x) if x is not None else None,
            gradients_wrt_inputs)
    captures_from_forward = [
        c for c in backwards_graph.external_captures
        if not isinstance(c, ops.EagerTensor) and c.graph is self._func_graph
    ]
    existing_outputs = object_identity.ObjectIdentitySet(
        self._func_graph.outputs)
    for capture in captures_from_forward:
        if capture not in existing_outputs:
            existing_outputs.add(capture)
            self._func_graph.outputs.append(capture)

    # The ordering of `backwards_graph.inputs` is important: inputs of
    # `backward_function` correspond to outputs (including
    # side outputs) of `self._tape_forward_function`.
backwards_graph.inputs = (
    gradients_wrt_outputs + backwards_graph.internal_captures)
backwards_graph.outputs.extend(
    grad
    for grad in nest.flatten(gradients_wrt_inputs, expand_composites=True)
    if grad is not None)
backwards_graph.structured_outputs = gradients_wrt_inputs

forward_function, backward_function = _create_forward_backward_with_graph(
    self._attrs, self._func_graph, backwards_graph)

if not input_tangents:
    # There is no need to special-case forwardprop, so we can return the
    # forward+backward pair we've created without further wrapping.
    exit((forward_function, self._func_graph, backward_function,
            # No forwardprop outputs.
            None, 0))
forward_wrapper = self._wrap_forward_function_with_jvps(
    forward_function, backward_function, inference_args, input_tangents)
(wrapped_backwards_graph,
 forward_wrapper) = self._wrap_backward_function_with_jvp_backprop(
     backward_function, gradients_wrt_outputs, forward_wrapper)
# Now that we've added new captures, we need to make sure forward outputs
# are in the same order the backward function expects them to be in:
# [inference outputs] + [jvps] + [side outputs] + [captures].
forward_wrapper = self._shuffle_forward_outputs(forward_wrapper)
(wrapped_forward_function,
 wrapped_backward_function) = _create_forward_backward_with_graph(
     self._attrs, forward_wrapper.graph, wrapped_backwards_graph)
if (len(inference_args) + len(input_tangents)
    != len(forward_wrapper.graph.inputs)):
    raise errors.InternalError(
        f"The forward graph had {len(forward_wrapper.graph.inputs)} inputs, "
        f"but we expected {len(inference_args) + len(input_tangents)} "
        f"({len(inference_args)} inference inputs and "
        f"{len(input_tangents)} input tangents).")
exit((wrapped_forward_function, forward_wrapper.graph,
        wrapped_backward_function, forward_wrapper.output_indices,
        len(forward_wrapper.output_tangents)))
