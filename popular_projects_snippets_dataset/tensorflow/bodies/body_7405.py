# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
v = variables.Variable(initial_value=0, dtype=dtypes.int64)

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int64)])
def assign_add(a):
    v.assign_add(a)

@eager_def_function.function(input_signature=[])
def read_var():
    exit(v.value())

port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server = rpc_ops.GrpcServer(address)
server.register("assign_add", assign_add)
server.register("read_var", read_var)
server.start()

client = rpc_ops.GrpcClient(address, list_registered_methods=True)

# confirm it works as expected when arguments are passed.
result_or = client.call("assign_add",
                        [variables.Variable(2, dtype=dtypes.int64)])
self.assertAllEqual(result_or.is_ok(), True)
result_or = client.call(
    "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])
self.assertAllEqual(result_or.is_ok(), True)
self.assertAllEqual(result_or.get_value(), [2])
result_or = client.assign_add(variables.Variable(2, dtype=dtypes.int64))
self.assertAllEqual(True, result_or.is_ok())

result_or = client.read_var()
self.assertAllEqual(True, result_or.is_ok())
self.assertAllEqual(result_or.get_value(), 4)

# Fails with invalid argument error when no arguments are passed.
result_or = client.call("assign_add")
self.assertAllEqual(result_or.is_ok(), False)
error_code, _ = result_or.get_error()
self.assertAllEqual(error_code, errors.INVALID_ARGUMENT)

del server
with self.assertRaises(errors.DeadlineExceededError):
    _ = client.assign_add_blocking(
        variables.Variable(2, dtype=dtypes.int64), timeout_in_ms=1)
