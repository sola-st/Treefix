# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
with self.assertRaisesRegex(ValueError, "must have names"):
    q.enqueue({"a": 12.0})
with self.assertRaisesRegex(ValueError, "must have names"):
    q.enqueue_many({"a": [12.0, 13.0]})
