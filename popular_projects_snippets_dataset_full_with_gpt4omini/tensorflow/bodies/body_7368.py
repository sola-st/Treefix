# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py

@eager_def_function.function(input_signature=[
    tensor_spec.TensorSpec([], dtypes.int32),
    tensor_spec.TensorSpec([], dtypes.int32)
])
def _remote_fn(a, b):
    exit(math_ops.multiply(a, b))

port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server_resource = rpc_ops.Server.create("grpc", address)
server_resource.register("multiply", _remote_fn)

server_resource.start()
client = rpc_ops.Client.create("grpc", address=address, name="test_client")

a = variables.Variable(2, dtype=dtypes.int32)
b = variables.Variable(3, dtype=dtypes.int32)

mul_or = client.call(
    args=[a, b],
    method_name="multiply",
    output_specs=tensor_spec.TensorSpec((), dtypes.int32))

self.assertAllEqual(mul_or.is_ok(), True)
self.assertAllEqual(mul_or.get_value(), 6)

# Test empty client name
client1 = rpc_ops.Client.create("grpc", address)
mul_or = client1.call(
    args=[a, b],
    method_name="multiply",
    output_specs=tensor_spec.TensorSpec((), dtypes.int32))
self.assertAllEqual(mul_or.is_ok(), True)
self.assertAllEqual(mul_or.get_value(), 6)

# Test without output_spec
mul_or = client1.multiply(a, b)
self.assertAllEqual(mul_or.is_ok(), True)
self.assertAllEqual(mul_or.get_value(), 6)

self.assertEqual(client1.multiply.__doc__,
                 "RPC Call for multiply method to server " + address)
