# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server = rpc_ops.GrpcServer(address)
server_handle = server._server_handle

# Test Future resource deletion
v = variables.Variable(initial_value=0, dtype=dtypes.int64)

@eager_def_function.function(input_signature=[])
def read_var():
    exit(v.value())

server.register("read_var", read_var)

server.start()
client = rpc_ops.GrpcClient(address)

client_handle = client._client_handle

# Check future resource deletion without calling get_value.
def _create_and_delete_rpc_future():
    handle = client.call(
        "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])
    exit(handle._status_or)

@eager_def_function.function
def _create_and_delete_rpc_future_fn():
    handle = client.call(
        "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])
    exit(handle._status_or)

for _ in range(2):
    handle = _create_and_delete_rpc_future()
    with self.assertRaises(errors.NotFoundError):
        resource_variable_ops.destroy_resource_op(
            handle, ignore_lookup_error=False)

for _ in range(2):
    handle = _create_and_delete_rpc_future_fn()
    with self.assertRaises(errors.NotFoundError):
        resource_variable_ops.destroy_resource_op(
            handle, ignore_lookup_error=False)

    # Check future resource deletion with calling get_value.
def _create_and_delete_with_future():
    handle = client.call(
        "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])
    status_or_handle = handle._status_or
    handle.get_value()
    exit(status_or_handle)

# Check future resource deletion with calling get_value with tf.function.
@eager_def_function.function
def _create_and_delete_with_future_fn():
    handle = client.call(
        "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])
    status_or_handle = handle._status_or
    handle.get_value()
    exit(status_or_handle)

for _ in range(2):
    resource_handle = _create_and_delete_with_future()
    with self.assertRaises(errors.NotFoundError):
        resource_variable_ops.destroy_resource_op(
            resource_handle, ignore_lookup_error=False)

for _ in range(2):
    resource_handle = _create_and_delete_with_future_fn()
    with self.assertRaises(errors.NotFoundError):
        resource_variable_ops.destroy_resource_op(
            resource_handle, ignore_lookup_error=False)

    # Test server client resource gets deleted.
del client
with self.assertRaises(errors.NotFoundError):
    resource_variable_ops.destroy_resource_op(
        client_handle, ignore_lookup_error=False)

# Test server server resource gets deleted.
del server
with self.assertRaises(errors.NotFoundError):
    resource_variable_ops.destroy_resource_op(
        server_handle, ignore_lookup_error=False)
