# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
v = variables.Variable(initial_value=0, dtype=dtypes.int64)

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int64)])
def assign_add(a):
    v.assign_add(a)

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int64)])
def assign(a):
    v.assign(a)

port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)
server = rpc_ops.GrpcServer(address)
server.register("assign", assign_add)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "assign is already registered."):
    # Reusing the same error name.
    server.register("assign", assign)
