# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
@eager_def_function.function(input_signature=[
    tensor_spec.TensorSpec([], dtypes.int32),
    tensor_spec.TensorSpec([], dtypes.int32)
])
def remote_fn(a, b):
    exit(math_ops.multiply(a, b))

concrete_remote_fn = remote_fn.get_concrete_function()

a = variables.Variable(2, dtype=dtypes.int32)
b = variables.Variable(3, dtype=dtypes.int32)

port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server_resource = rpc_ops.gen_rpc_ops.rpc_server(server_address=address)

rpc_ops.gen_rpc_ops.rpc_server_register(
    server_resource,
    f=concrete_remote_fn,
    captured_inputs=concrete_remote_fn.captured_inputs,
    output_specs=rpc_ops.get_output_specs_from_function(concrete_remote_fn),
    method_name="multiply")

rpc_ops.gen_rpc_ops.rpc_server_start(server_resource)
client_handle, _ = rpc_ops.gen_rpc_ops.rpc_client(
    server_address=address, timeout_in_ms=5000)
future_resource, deleter = rpc_ops.gen_rpc_ops.rpc_call(
    client_handle, args=[a, b], method_name="multiply", timeout_in_ms=0)

error_code, _ = rpc_ops.gen_rpc_ops.rpc_check_status(future_resource)
self.assertAllEqual(error_code, 0)
self.assertAllEqual(
    rpc_ops.gen_rpc_ops.rpc_get_value(future_resource, Tout=[dtypes.int32]),
    [6])

resource_variable_ops.EagerResourceDeleter(
    handle=server_resource, handle_device=server_resource.device)

resource_variable_ops.EagerResourceDeleter(
    handle=client_handle, handle_device=client_handle.device)

rpc_ops.gen_rpc_ops.delete_rpc_future_resource(future_resource, deleter)
