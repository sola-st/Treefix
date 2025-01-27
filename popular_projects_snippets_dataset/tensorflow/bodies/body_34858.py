# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))

    elems = [10.0, 20.0, 30.0]
    elems_ave = sum(elems) / len(elems)
    accum_ops = [q.apply_grad((x,), local_step=0) for x in elems]
    takeg_t = q.take_grad(3)

    def apply_grad():
        time.sleep(1.0)
        for accum_op in accum_ops:
            self.evaluate(accum_op)

    return_array = []

    def take_grad():
        return_array.append(self.evaluate(takeg_t))

    accum_thread = self.checkedThread(target=apply_grad)
    takeg_thread = self.checkedThread(target=take_grad)
    accum_thread.start()
    takeg_thread.start()
    accum_thread.join()
    takeg_thread.join()

    self.assertEqual([elems_ave], return_array)
