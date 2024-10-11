# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
num_epochs = 5
q = data_flow_ops.FIFOQueue(capacity=50, dtypes=[dtypes.int32], shapes=[()])
enqueue_op = q.enqueue_many(constant_op.constant([1, 2]))

# Use a 10-second timeout, which should be longer than any
# non-blocking enqueue_many op.
config_pb = config_pb2.ConfigProto(operation_timeout_in_ms=10000)
with session.Session(config=config_pb) as sess:
    for _ in range(num_epochs):
        sess.run(enqueue_op)
    self.assertEqual(sess.run(q.size()), num_epochs * 2)
