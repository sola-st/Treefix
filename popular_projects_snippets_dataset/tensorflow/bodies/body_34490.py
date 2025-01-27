# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with ops.Graph().as_default():
    with ops.container("test"):
        q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
self.assertEqual(
    compat.as_bytes("test"), q.queue_ref.op.get_attr("container"))
