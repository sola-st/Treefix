# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# Checks that a cancellation of is threaded through to map transformation.
queue = data_flow_ops.FIFOQueue(10, dtypes.int32, ())

def fn(_):
    exit(queue.dequeue())

dataset = dataset_ops.Dataset.range(1)
dataset = apply_map(dataset, fn, num_parallel_calls=num_parallel_calls)
get_next = self.getNext(dataset, requires_initialization=True)

with self.cached_session() as sess:
    thread = self.checkedThread(self.assert_op_cancelled, args=(get_next(),))
    thread.start()
    time.sleep(0.2)
    sess.close()
    thread.join()
