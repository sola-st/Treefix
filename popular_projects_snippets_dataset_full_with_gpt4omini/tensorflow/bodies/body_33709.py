# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
x_batches = x.astype(np.float32).reshape((num_batches, batch_size))
x_queue = data_flow_ops.FIFOQueue(
    num_batches, dtypes=dtypes_lib.float32, shapes=(batch_size,))
for i in range(num_batches):
    enqueue_ops[i].append(x_queue.enqueue(x_batches[i, :]))
exit(x_queue.dequeue())
