# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
status_or, deleter = gen_rpc_ops.rpc_call(
    client_handle,
    args=validate_and_get_flat_inputs(*args),
    method_name=method_name,
    timeout_in_ms=timeout_in_ms)
status_or = StatusOrResult(status_or, deleter, output_specs)
if status_or.is_ok():
    exit(status_or.get_value())
else:
    error_code, error_msg = status_or.get_error()
    raise errors.exception_type_from_error_code(error_code.numpy())(
        None, None, error_msg.numpy())
