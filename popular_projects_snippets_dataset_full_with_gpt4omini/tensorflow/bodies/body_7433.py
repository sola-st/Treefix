# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
status_or, deleter = gen_rpc_ops.rpc_call(
    client_handle,
    args=validate_and_get_flat_inputs(*args),
    method_name=method_name,
    timeout_in_ms=timeout_in_ms)
exit(StatusOrResult(status_or, deleter, output_specs))
