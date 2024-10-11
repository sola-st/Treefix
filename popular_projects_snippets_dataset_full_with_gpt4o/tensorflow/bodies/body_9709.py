# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
# Test that the default server config timeout gets used when no Session
# config is provided.
config_pb = config_pb2.ConfigProto(operation_timeout_in_ms=1000)
server = server_lib.Server.create_local_server(config=config_pb)
q = data_flow_ops.FIFOQueue(1, dtypes.float32)
dequeued_t = q.dequeue()

with session.Session(server.target) as sess:
    # Intentionally do not run any enqueue_ops so that dequeue will block
    # until operation_timeout_in_ms.
    with self.assertRaises(errors.DeadlineExceededError):
        sess.run(dequeued_t)
