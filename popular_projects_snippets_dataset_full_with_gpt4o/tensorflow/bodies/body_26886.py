# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sleep_test.py
sleep_microseconds = int(1e6) * 1000
ds = dataset_ops.Dataset.range(1)
ds = ds.apply(testing.sleep(sleep_microseconds))
ds = ds.prefetch(1)
get_next = self.getNext(ds, requires_initialization=True)

with self.cached_session() as sess:
    thread = self.checkedThread(self.assert_op_cancelled, args=(get_next(),))
    thread.start()
    time.sleep(0.2)
    sess.close()
    thread.join()
