# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))

    local_steps = range(1000, 1005)
    accum_ops = [q.apply_grad((0.0 + x,), local_step=x) for x in local_steps]

    for ls in local_steps:
        set_global_step_op = q.set_global_step(ls)
        set_global_step_op.run()

        for accum_op in accum_ops:
            accum_op.run()
        takeg_t = q.take_grad(1)

        val = self.evaluate(takeg_t)
        self.assertEqual(0.0 + sum(x for x in local_steps
                                   if x >= ls) / sum(1 for x in local_steps
                                                     if x >= ls), val)
