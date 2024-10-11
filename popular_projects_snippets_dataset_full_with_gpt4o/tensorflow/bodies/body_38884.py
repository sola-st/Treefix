# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([2, 2]))
    elems = [e + 1 for e in range(10)]
    accum_ops = []
    for e in elems:
        v = _indexedslice(np.array([[0, 0], [e, 0]]).astype(np.float32))
        accum_ops.append(q.apply_indexed_slices_grad(v, local_step=e - 1))
    takeg_t = q.take_indexed_slices_grad(1)

    results = []

    def apply_indexed_slices_grad():
        for accum_op in accum_ops:
            time.sleep(1.0)
            self.evaluate(accum_op)

    apply_indexed_slices_grad_thread = self.checkedThread(
        target=apply_indexed_slices_grad)

    def take_grad():
        t = self.evaluate(takeg_t)
        results.append(t)

    threads = [self.checkedThread(target=take_grad) for _ in range(10)]

    for thread in threads:
        thread.start()
    apply_indexed_slices_grad_thread.start()

    for thread in threads:
        thread.join()
    apply_indexed_slices_grad_thread.join()

    for i in range(len(accum_ops)):
        self._assertEqual_nparray(
            np.array([[0, 0], [elems[i], 0]]), results[i], sess)
