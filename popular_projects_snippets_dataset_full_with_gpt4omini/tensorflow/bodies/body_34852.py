# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))
    elems = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    accum_ops = [q.apply_grad((x,), local_step=0) for x in elems]
    takeg_t = q.take_grad(1)

    def apply_grad(accum_op):
        self.evaluate(accum_op)

    threads = [
        self.checkedThread(
            target=apply_grad, args=(o,)) for o in accum_ops
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    val = self.evaluate(takeg_t)

    self.assertEqual(val, sum(elems) / len(elems))
