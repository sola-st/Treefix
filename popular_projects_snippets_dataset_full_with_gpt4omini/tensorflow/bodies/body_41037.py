# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Converts numpy array inputs to tensors."""
flat_inputs = composite_tensor_utils.flatten_with_variables(inputs)

# Check for NumPy arrays in arguments and convert them to Tensors.
# TODO(nareshmodi): Skip ndarray conversion to tensor altogether, perhaps
# finding a way to store them directly in the cache key (currently not
# possible since ndarrays are not hashable).
need_packing = False
filtered_flat_inputs = []
for index, value in enumerate(flat_inputs):
    if isinstance(value,
                  (ops.Tensor, resource_variable_ops.BaseResourceVariable)):
        filtered_flat_inputs.append(value)
    elif hasattr(value, "__array__") and not (
        hasattr(value, "_should_act_as_resource_variable") or
        isinstance(value, (np.str_, type, composite_tensor.CompositeTensor))):
        # This case is equivalent to _is_ndarray(value) == True
        a = value.__array__()
        if not isinstance(a, np.ndarray):
            raise TypeError(f"The output of __array__ must be an np.ndarray, "
                            f"got {type(a)} from {value}.")
        flat_inputs[index] = constant_op.constant(a)
        filtered_flat_inputs.append(flat_inputs[index])
        need_packing = True
if need_packing:
    exit(nest.pack_sequence_as(
        structure=inputs,
        flat_sequence=nest.flatten(flat_inputs, expand_composites=True),
        expand_composites=True))
else:
    exit(inputs)
