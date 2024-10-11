# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def test_dict(val):
    exit({"key": val})

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def is_positive(a):
    if a > 0:
        exit(True)
    exit(False)

@eager_def_function.function(input_signature=[])
def do_nothing():
    exit([])

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def test_nested_structure(v):
    exit({"test": (v, [v, v]), "test1": (v,)})

port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server_resource = rpc_ops.GrpcServer(address)

server_resource.register("test_dict", test_dict)
server_resource.register("is_positive", is_positive)
server_resource.register("test_nested_structure", test_nested_structure)
server_resource.register("do_nothing", do_nothing)

server_resource.start()

client = rpc_ops.GrpcClient(
    address=address, name="test_client", list_registered_methods=True)

a = variables.Variable(2, dtype=dtypes.int32)

result_or = client.test_dict(a)
self.assertAllEqual(result_or.is_ok(), True)
nest.map_structure(self.assertAllEqual, result_or.get_value(), {"key": 2})

result_or = client.is_positive(a)
self.assertTrue(result_or.is_ok())
self.assertTrue(result_or.get_value())

result_or = client.test_nested_structure(a)
self.assertAllEqual(result_or.is_ok(), True)
nest.map_structure(self.assertAllEqual, result_or.get_value(), {
    "test": (2, [2, 2]),
    "test1": (2,)
})

result_or = client.do_nothing()
self.assertAllEqual(result_or.is_ok(), True)
self.assertAllEqual(result_or.get_value(), [])
