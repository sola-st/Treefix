# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Create a backward function given `outputs` from the forward function."""
capture_mapping = dict(
    zip((ops.tensor_id(t) for t in forward_graph.outputs), outputs))
captured_inputs = backward.captured_inputs
remapped_captures = [
    capture_mapping.get(ops.tensor_id(capture), capture)
    for capture in captured_inputs
]
if any(t.graph is forward_graph for t in remapped_captures
       if not isinstance(t, ops.EagerTensor)):
    incorrect_mapping = [t for t in remapped_captures
                         if (not isinstance(t, ops.EagerTensor) and
                             t.graph is not forward_graph)]
    raise errors.InternalError("Failed to map all backward graph captures to "
                               "the forward graph. Incorrectly mapped: "
                               f"{incorrect_mapping}.")
# We may need to use zeros_like to get a zero for variant Tensors with
# unconnected gradients. We do that in advance so we don't have to hold on
# to the outputs themselves, which may not be needed otherwise.
variant_zeros_like = {}
backward_function_inputs = (len(backward.inputs) - len(captured_inputs))
recorded_outputs = []
trainable_recorded_outputs = 0
skip_positions = []
if self._num_forwardprop_outputs and not self._need_gradients_for_jvps:
    relevant_outputs = (
        outputs[:self._num_inference_outputs]
        + outputs[self._num_inference_outputs
                  + self._num_forwardprop_outputs:])
else:
    relevant_outputs = outputs
for output_index, output in enumerate(relevant_outputs):
    if trainable_recorded_outputs < backward_function_inputs:
        recorded_outputs.append(output)
    if backprop_util.IsTrainable(output):
        trainable_recorded_outputs += 1
    else:
        skip_positions.append(output_index)
    if output.dtype == dtypes.variant:
        variant_zeros_like[output_index] = default_gradient.zeros_like(output)

def _backward_function_wrapper(*args):
    """Process output gradients and call the backward function."""
    if not backward.outputs:
        exit(backward.structured_outputs)

    processed_args = []
    input_index = 0
    for output_index, arg in enumerate(args):
        # Convert IndexedSlices to dense tensors. The IndexedSlices optimization
        # is only really effective when doing tf.gather(variable) as the
        # adjoint functions for most operations are unlikely to preserve the
        # sparsity in IndexedSlices.
        if isinstance(arg, indexed_slices.IndexedSlices):
            arg = ops.convert_to_tensor(arg)
        if output_index in skip_positions:
            continue
        if arg is None:
            # We're calling a (non-polymorphic) ConcreteFunction, so we need to
            # have a Tensor value for each Tensor we thought would be trainable
            # based on its dtype, even if it ended up being unconnected.
            input_placeholder = backward.inputs[
                input_index]
            if input_placeholder.dtype == dtypes.variant:
                arg = variant_zeros_like[output_index]
            else:
                arg = array_ops.zeros(
                    *default_gradient.shape_and_dtype(input_placeholder))
        processed_args.append(arg)
        input_index += 1
        if input_index >= backward_function_inputs:
            break
    exit(backward._call_flat(  # pylint: disable=protected-access
        processed_args, remapped_captures))

exit((_backward_function_wrapper, recorded_outputs))
