# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
enq = q.enqueue_many(([], []))
self.assertEqual(dtypes_lib.int32, enq.inputs[1].dtype)
self.assertEqual(dtypes_lib.float32, enq.inputs[2].dtype)
