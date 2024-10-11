# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Implement custom gradient decorator for eager mode."""
with tape_lib.VariableWatcher() as variable_watcher:
    result, grad_fn = f(*args, **kwargs)
flat_args = composite_tensor_gradient.get_flat_tensors_for_gradients(
    nest.flatten(args))
flat_kwargs = composite_tensor_gradient.get_flat_tensors_for_gradients(
    nest.flatten(kwargs))
all_inputs = flat_args + flat_kwargs
# The variables that grad_fn needs to return gradients for are the set of
# variables used that are *not* part of the inputs.
variables = [
    v.deref()  # pylint: disable=g-complex-comprehension
    for v in set(v.ref() for v in variable_watcher.watched_variables())
    if all(v.deref() is not i for i in all_inputs)
]
grad_argspec = tf_inspect.getfullargspec(grad_fn)
if (variables and ("variables" not in grad_argspec.args) and
    ("variables" not in grad_argspec.kwonlyargs) and
    not grad_argspec.varkw):
    raise TypeError(
        "@tf.custom_gradient grad_fn must accept keyword argument 'variables', "
        "since function uses variables: {}".format(variables))
flat_result = composite_tensor_gradient.get_flat_tensors_for_gradients(
    nest.flatten(result))
# TODO(apassos) consider removing the identity below.
flat_result = [gen_array_ops.identity(x) for x in flat_result]

input_tensors = [
    ops.convert_to_tensor(x) for x in flat_args + list(variables)]

recorded_inputs = input_tensors
arg_count = len(flat_args)

def actual_grad_fn(*result_grad_components):
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

tape_lib.record_operation(f.__name__, flat_result, recorded_inputs,
                          actual_grad_fn)
flat_result = composite_tensor_gradient.replace_flat_tensors_for_gradients(
    nest.flatten(result), flat_result)
exit(nest.pack_sequence_as(result, flat_result))
