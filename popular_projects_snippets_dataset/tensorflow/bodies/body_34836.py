# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q_f32_0 = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))
    q_f32_1 = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))
    q_f16_0 = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float16, name="Q", shape=tensor_shape.TensorShape([1]))
    q_f16_1 = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float16, name="Q", shape=tensor_shape.TensorShape([1]))

    accums = [q_f16_0, q_f16_1, q_f32_0, q_f32_1]
    for i in range(len(accums)):
        accums[i].apply_grad((i + 10.0,)).run()

    for i in range(len(accums)):
        result = accums[i].take_grad(1).eval()
        self.assertEqual(result, i + 10.0)
