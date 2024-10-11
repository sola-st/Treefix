# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session(), self.test_scope():
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    with self.assertRaisesRegex(ValueError, "must have names"):
        q.enqueue({"a": 12.0})
