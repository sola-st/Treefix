# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py
del x
queue = data_flow_ops.FIFOQueue(10, dtypes.int32, ())
# Blocking
exit(queue.dequeue_many(5))
