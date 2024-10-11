# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32,
        name="Q",
        shape=tensor_shape.TensorShape([1]),
        reduction_type="SUM")

    elems = [10.0, 20.0]
    elems_sum = 30.0
    accum_ops = [q.apply_grad((x,), local_step=0) for x in elems]
    takeg_t = q.take_grad(1)

    for accum_op in accum_ops:
        accum_op.run()

    val = self.evaluate(takeg_t)
    self.assertEqual(elems_sum, val)

    elems = [20.0, 30.0]
    elems_sum = 50.0
    accum_ops = [q.apply_grad((x,), local_step=1) for x in elems]
    takeg_t = q.take_grad(1)

    for accum_op in accum_ops:
        accum_op.run()

    val = self.evaluate(takeg_t)
    self.assertEqual(elems_sum, val)
