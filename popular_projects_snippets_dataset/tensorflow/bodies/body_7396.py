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

server_resource.register("remote_fn", _remote_fn)

server_resource.start()
client = rpc_ops.GrpcClient(address=address, name="test_client")

a = variables.Variable(2, dtype=dtypes.int32)
b = variables.Variable(3, dtype=dtypes.int32)

@eager_def_function.function
def call_fn():
    result_or = client.call(
        args=[a, b],
        method_name="remote_fn",
        output_specs=[tensor_spec.TensorSpec([], dtypes.int32)])

    self.assertAllEqual(True, result_or.is_ok())
    result = result_or.get_value()
    self.assertEqual(len(result), 1)  # Call returns a list(tensors)
    # TODO(ishark): Shape for output tensor is unknown currently.
    # Add attribute for capturing TensorSpec for output and enable
    # check below:
    # self.assertIsNotNone(result[0].shape.rank)
    exit(result)

self.assertAllEqual(call_fn(), [6])
