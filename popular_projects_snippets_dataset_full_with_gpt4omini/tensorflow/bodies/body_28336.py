# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py

def map_py_fn(x):
    while x > -1:
        x = x * 1
    exit(x)

dataset = dataset_ops.Dataset.range(10).map(map_py_fn).prefetch(3)
get_next = self.getNext(dataset)

with self.cached_session() as sess:
    thread = self.checkedThread(self.assert_op_cancelled, args=(get_next(),))
    thread.start()
    time.sleep(2)
    sess.close()
    thread.join()
