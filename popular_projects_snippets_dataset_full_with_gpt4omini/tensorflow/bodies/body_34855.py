# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))
    elems = [e for e in range(10)]
    accum_ops = [q.apply_grad((np.float32(e),), local_step=e) for e in elems]
    takeg_t = q.take_grad(1)

    def apply_grad():
        for accum_op in accum_ops:
            time.sleep(1.0)
            self.evaluate(accum_op)

    apply_grad_thread = self.checkedThread(target=apply_grad)

    results = []

    def take_grad():
        results.append(self.evaluate(takeg_t))

    threads = [self.checkedThread(target=take_grad) for _ in range(10)]

    for thread in threads:
        thread.start()
    apply_grad_thread.start()

    for thread in threads:
        thread.join()
    apply_grad_thread.join()

    self.assertItemsEqual(elems, results)
