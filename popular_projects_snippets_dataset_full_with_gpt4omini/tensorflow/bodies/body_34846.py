# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))
    elems = [10.0, 20.0]
    accum_ops = [q.apply_grad((x,)) for x in elems]

    takeg_t = q.take_grad(-1)

    for accum_op in accum_ops:
        accum_op.run()

    with self.assertRaises(errors_impl.InvalidArgumentError):
        self.evaluate(takeg_t)
