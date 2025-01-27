# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)

# Create client succeeds before server start and registration
client = rpc_ops.GrpcClient(address)

# Create client with list_registered_methods fails before server is started.
with self.assertRaises(errors.DeadlineExceededError):
    rpc_ops.GrpcClient(
        address,
        name="client1",
        list_registered_methods=True,
        timeout_in_ms=1)

v = variables.Variable(initial_value=0, dtype=dtypes.int64)

@eager_def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int64)])
def assign_add(a):
    v.assign_add(a)

@eager_def_function.function(input_signature=[])
def read_var():
    exit(v.value())

server = rpc_ops.GrpcServer(address)

def start_server():
    # Delay server start to test whether client creation also waits
    # till server is up.
    time.sleep(1)
    server.register("assign_add", assign_add)
    server.start()

t = threading.Thread(target=start_server)
t.start()

# Create same "client1" again should succeed.
client1_with_listed_methods = rpc_ops.GrpcClient(
    address, name="client1", list_registered_methods=True)

result_or = client1_with_listed_methods.assign_add(
    variables.Variable(2, dtype=dtypes.int64))
self.assertAllEqual(result_or.is_ok(), True)

result_or = client.call("assign_add",
                        [variables.Variable(2, dtype=dtypes.int64)])
self.assertAllEqual(result_or.is_ok(), True)

# Create client with registered methods
client2_with_listed_methods = rpc_ops.GrpcClient(
    address=address, name="client2", list_registered_methods=True)

result_or = client2_with_listed_methods.assign_add(
    variables.Variable(2, dtype=dtypes.int64))
self.assertAllEqual(result_or.is_ok(), True)

self.assertAllEqual(v, 6)

# Register new method after server started.
with self.assertRaisesRegex(
    errors.FailedPreconditionError,
    "All methods must be registered before starting the server"):
    server.register("read_var", read_var)
