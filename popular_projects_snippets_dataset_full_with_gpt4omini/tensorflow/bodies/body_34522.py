# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session() as session:
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=3)
    g_ta_0 = ta.grad("grad")
    g_ta_1 = ta.grad("grad")

    with ops.control_dependencies([g_ta_0.write(0, [[4.0, 5.0]]).flow]):
        # Write with one gradient handle, read with another copy of it
        r1_0 = g_ta_1.read(0)

    t_g_ta_0, t_g_ta_1, d_r1_0 = session.run(
        [g_ta_0.handle.op, g_ta_1.handle.op, r1_0])
    self.assertAllEqual(t_g_ta_0, t_g_ta_1)
    self.assertAllEqual([[4.0, 5.0]], d_r1_0)
