# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
if not control_flow_util.ENABLE_CONTROL_FLOW_V2:
    self.skipTest("Legacy TensorArray does not support double derivatives.")
with self.test_session() as session:
    x = constant_op.constant(4.0)

    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=1,
        infer_shape=False)
    w0 = ta.write(0, x)
    r0 = w0.read(0)
    y = r0 * r0

    g1 = gradients_impl.gradients(ys=[y], xs=[x])
    g2 = gradients_impl.gradients(ys=[g1], xs=[x])
    self.assertAllEqual([2.0], session.run(g2))
