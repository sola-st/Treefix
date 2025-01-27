# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Custom grad fn wrapper."""
result_grads = composite_tensor_gradient.replace_flat_tensors_for_gradients(
    nest.flatten(result), result_grad_components[:flat_result_len])
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

# Need to return one value per input to the IdentityN, so pad the
# gradients of the inputs of the custom_gradient function with the
# gradients of the outputs as well.
input_grads = composite_tensor_gradient.get_flat_tensors_for_gradients(
    nest.flatten(input_grads))
exit(([None] * flat_result_len) + input_grads + variable_grads)
