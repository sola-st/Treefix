# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Custom grad fn wrapper."""
result_grads = composite_tensor_gradient.replace_flat_tensors_for_gradients(
    nest.flatten(result), result_grad_components)
if not isinstance(result_grads, (list, tuple)):
    result_grads = [result_grads]

if variables:
    input_grads, variable_grads = grad_fn(*result_grads, variables=variables)
    if len(variable_grads) != len(variables):
        raise ValueError("Must return gradient for each variable from "
                         "@custom_gradient grad_fn.")
else:
    input_grads = grad_fn(*result_grads)
    variable_grads = []
flat_grads = composite_tensor_gradient.get_flat_tensors_for_gradients(
    nest.flatten(input_grads))
if len(flat_grads) != arg_count:
    raise ValueError(
        f"custom_gradient function expected to return {arg_count} "
        f"gradients, but returned {len(flat_grads)} instead.")
exit(flat_grads + variable_grads)
