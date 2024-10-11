# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
with ops.device("/device:cpu:1"):
    v = variables.Variable(initial_value=0, dtype=dtypes.int64)

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int64)])
def assign_add(a):
    v.assign_add(a)

with ops.device("/device:CPU:0"):
    port = portpicker.pick_unused_port()
    address = "localhost:{}".format(port)
    server = rpc_ops.GrpcServer(address)
    server.register("assign_add", assign_add)
    server.start()

    client = rpc_ops.GrpcClient(address, list_registered_methods=True)
    result_or = client.assign_add(variables.Variable(2, dtype=dtypes.int64))
    self.assertAllEqual(result_or.is_ok(), True)

self.assertAllEqual(v, 2)
