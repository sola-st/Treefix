# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
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
