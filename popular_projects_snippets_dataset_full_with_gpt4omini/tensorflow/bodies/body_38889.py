# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32,
        name="Q",
        shape=tensor_shape.TensorShape([1, 2, 3]))
    takeg_t = q.take_indexed_slices_grad(1)

    takeg_thread = self.checkedThread(
        self._blocking_takeg, args=(sess, takeg_t))

    takeg_thread.start()

    time.sleep(1.0)

    sess.close()  # Will cancel blocked operation

    takeg_thread.join()
