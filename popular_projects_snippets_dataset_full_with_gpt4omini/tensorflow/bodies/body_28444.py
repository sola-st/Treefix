# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
ds = dataset_ops.Dataset.from_tensors(1).repeat()
result = ds.reduce(0, lambda x, y: x + y)
with self.cached_session() as sess:
    # The `result` op is guaranteed to not complete before cancelled because
    # the dataset that is being reduced is infinite.
    thread = self.checkedThread(self.assert_op_cancelled, args=(result,))
    thread.start()
    time.sleep(0.2)
    sess.close()
    thread.join()
