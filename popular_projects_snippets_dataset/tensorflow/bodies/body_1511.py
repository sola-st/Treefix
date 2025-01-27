# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session(), self.test_scope():
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    enqueue_op = q.enqueue((10.0,))
    enqueue_op.run()
