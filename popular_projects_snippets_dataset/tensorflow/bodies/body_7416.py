# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
elements = np.random.randint(100, size=[200])

with ops.device("/device:CPU:1"):
    queue = data_flow_ops.FIFOQueue(200, dtypes.int64, shapes=[])

@eager_def_function.function()
def populate_queue():
    queue.enqueue_many(elements)
    queue.close()

with ops.device("/device:CPU:0"):
    port = portpicker.pick_unused_port()
    address = "localhost:{}".format(port)
    server = rpc_ops.GrpcServer(address)
    server.register("populate_queue", populate_queue)
    server.start()

    client = rpc_ops.GrpcClient(address, list_registered_methods=True)
    client.populate_queue()

for e in elements:
    self.assertAllEqual(e, queue.dequeue())
