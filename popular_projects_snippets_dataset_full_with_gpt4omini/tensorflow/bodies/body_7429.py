# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Method for registering functions."""

if isinstance(func, def_function.Function):
    if func._function_spec.arg_names:  # pylint: disable=protected-access
        if func.input_signature is None:
            raise ValueError("Input signature not specified for the function.")
    concrete_fn = func.get_concrete_function()
    gen_rpc_ops.rpc_server_register(
        self._server_handle,
        method_name=method_name,
        captured_inputs=concrete_fn.captured_inputs,
        input_specs=get_input_specs_from_function(concrete_fn),
        output_specs=get_output_specs_from_function(concrete_fn),
        f=concrete_fn)
elif isinstance(func, tf_function.ConcreteFunction):
    gen_rpc_ops.rpc_server_register(
        self._server_handle,
        method_name=method_name,
        captured_inputs=func.captured_inputs,
        input_specs=get_input_specs_from_function(func),
        output_specs=get_output_specs_from_function(func),
        f=func)
else:
    # Python functions
    # TODO(b/186762191): Add an implementation to support python functions.
    raise ValueError("Only TF functions are supported with Register method")
