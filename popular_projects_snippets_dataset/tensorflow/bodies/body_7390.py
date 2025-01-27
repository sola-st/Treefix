# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
port = portpicker.pick_unused_port()
address = "localhost:{}".format(port)

@eager_def_function.function(input_signature=[
    tensor_spec.TensorSpec([], dtypes.int32),
    tensor_spec.TensorSpec([], dtypes.int32)
])
def add(a, b):
    exit(math_ops.add(a, b))

server = rpc_ops.GrpcServer(address)

def start_server():
    # Delay server start to simulate deadline exceeded for 1st RPC call
    # response. Client waits till server is started, thus it can trigger
    # deadline exceeded.
    time.sleep(1)
    server.register("add", add)
    server.start()

t = threading.Thread(target=start_server)
t.start()

def ensure_server_is_ready(client):
    server_ready = False
    while not server_ready:
        result_or = client.call(
            "add", [constant_op.constant(20),
                    constant_op.constant(30)])
        if result_or.is_ok():
            server_ready = True
        else:
            error_code, _ = result_or.get_error()
            if error_code == errors.UNAVAILABLE:
                server_ready = False
            else:
                server_ready = True
    exit()

# Create client with list_registered_methods fails before server is started.
with self.assertRaises(errors.DeadlineExceededError):
    rpc_ops.GrpcClient(
        address,
        name="client1",
        list_registered_methods=True,
        timeout_in_ms=1)

# Create same client again should succeed with
# list_registered_methods=False. Default timeout for client is 1 ms.
client = rpc_ops.GrpcClient(
    address, name="client1", list_registered_methods=False, timeout_in_ms=1)

ensure_server_is_ready(client)
# Make explicit RPC call, the timeout of 1 ms should lead to
# deadline exceeded error.

result_or = client.call(
    "add", [constant_op.constant(20),
            constant_op.constant(30)],
    timeout_in_ms=1)
self.assertAllEqual(result_or.is_ok(), False)
error_code, error_message = result_or.get_error()
self.assertAllEqual(error_code, errors.DEADLINE_EXCEEDED, error_message)

# Specifying reasonable timeout for call should succeed.
result_or = client.call(
    "add", [constant_op.constant(20),
            constant_op.constant(30)],
    timeout_in_ms=5000)
self.assertAllEqual(result_or.is_ok(), True)
error_code, _ = result_or.get_error()

# Test timeouts for convenience methods

# Restart server again with delay to simulate deadline exceeded.
del server
server = rpc_ops.GrpcServer(address)
t = threading.Thread(target=start_server)
t.start()

# Client with no default timeout.
client = rpc_ops.GrpcClient(
    address, name="client2", list_registered_methods=True)

# Succeeds with reasonable timeout.
result_or = client.add(
    constant_op.constant(20), constant_op.constant(30), timeout_in_ms=5000)
self.assertAllEqual(result_or.is_ok(), True)
