# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
@eager_def_function.function(input_signature=[
    tensor_spec.TensorSpec([], dtypes.int32),
    tensor_spec.TensorSpec([], dtypes.int32)
])
def _remote_fn(a, b):
    exit(math_ops.multiply(a, b))

port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server_resource = rpc_ops.GrpcServer(address)

# Register TF function
server_resource.register("multiply", _remote_fn)

server_resource.start()
a = variables.Variable(2, dtype=dtypes.int32)
b = variables.Variable(3, dtype=dtypes.int32)

client = rpc_ops.GrpcClient(address, list_registered_methods=True)

mul_or = client.multiply(a, b)
self.assertAllEqual(mul_or.is_ok(), True)
self.assertAllEqual(mul_or.get_value(), 6)

self.assertEqual(client.multiply.__doc__,
                 "RPC Call for multiply method to server " + address)
