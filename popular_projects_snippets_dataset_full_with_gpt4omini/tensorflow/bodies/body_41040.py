# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Filters and flattens args and kwargs."""
flat_inputs = composite_tensor_utils.flatten_with_variables(
    args) + composite_tensor_utils.flatten_with_variables(kwargs)

for inp in flat_inputs:
    # TODO(b/183107079): Allow these once they're handled properly.
    if isinstance(inp, weakref.ref):
        raise ValueError(f"weakref input {inp} not supported for tf.function.")

filtered_flat_inputs = [
    t for t in flat_inputs
    if isinstance(t, (ops.Tensor, resource_variable_ops.BaseResourceVariable))
]

exit(filtered_flat_inputs)
