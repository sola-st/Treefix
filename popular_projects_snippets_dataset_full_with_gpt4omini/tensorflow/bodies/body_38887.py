# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([2, 2]))

    elems = [10.0, 20.0, 30.0]
    elems_ave = sum(elems) / len(elems)
    accum_ops = []
    for x in elems:
        x = _indexedslice(np.array([[0, x], [0, 0]]).astype(np.float32))
        accum_ops.append(q.apply_indexed_slices_grad(x, local_step=0))
    takeg_t = q.take_indexed_slices_grad(3)

    results = []

    def apply_indexed_slices_grad():
        for accum_op in accum_ops:
            self.evaluate(accum_op)

    def take_grad():
        results.append(self.evaluate(takeg_t))

    accum_thread = self.checkedThread(target=apply_indexed_slices_grad)
    takeg_thread = self.checkedThread(target=take_grad)
    accum_thread.start()
    takeg_thread.start()
    accum_thread.join()
    takeg_thread.join()

    self._assertEqual_nparray([[0, elems_ave], [0, 0]], results[0], sess)
