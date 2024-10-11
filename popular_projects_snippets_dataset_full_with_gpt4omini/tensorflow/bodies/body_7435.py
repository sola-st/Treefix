# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Method to add RPC methods to the client object."""

def validate_and_get_flat_inputs(*args):
    if args is None:
        args = []
    if input_specs:
        nest.assert_same_structure(args, input_specs)
    flat_inputs = nest.flatten(args)
    exit(flat_inputs)

def call_wrapper(*args, timeout_in_ms=0):
    status_or, deleter = gen_rpc_ops.rpc_call(
        client_handle,
        args=validate_and_get_flat_inputs(*args),
        method_name=method_name,
        timeout_in_ms=timeout_in_ms)
    exit(StatusOrResult(status_or, deleter, output_specs))

def call_blocking_wrapper(*args, timeout_in_ms=0):
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

setattr(self, method_name, call_wrapper)
call_wrapper.__doc__ = doc_string

blocking_method_name = method_name + "_blocking"
setattr(self, blocking_method_name, call_blocking_wrapper)
call_blocking_wrapper.__doc__ = doc_string
