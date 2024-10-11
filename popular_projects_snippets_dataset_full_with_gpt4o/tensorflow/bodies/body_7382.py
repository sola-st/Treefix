# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py

@eager_def_function.function(input_signature=[{
    "a": tensor_spec.TensorSpec([], dtypes.int32),
    "b": tensor_spec.TensorSpec([], dtypes.int32)
}])
def test_input_dict(value):
    exit(math_ops.add(value["a"], value["b"]))

port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server_resource = rpc_ops.GrpcServer(address)

server_resource.register("test_input_dict", test_input_dict)

server_resource.start()

client = rpc_ops.GrpcClient(
    address=address, name="test_client", list_registered_methods=True)
a = variables.Variable(2, dtype=dtypes.int32)
b = variables.Variable(3, dtype=dtypes.int32)
result_or = client.test_input_dict({"a": a, "b": b})
self.assertAllEqual(result_or.is_ok(), True)
self.assertAllEqual(result_or.get_value(), 5)

with self.assertRaises(TypeError):
    client.test_input_dict([a, b])
