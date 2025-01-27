# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32), shapes=((), ()), name="B")
    take_t = b.take_many(1, allow_small_batch=True)
    self.evaluate(b.close(cancel))
    with self.assertRaisesOpError("is closed and has insufficient elements"):
        self.evaluate(take_t)
