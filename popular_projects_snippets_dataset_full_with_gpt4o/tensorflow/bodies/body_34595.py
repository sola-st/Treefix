# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
n_time = 1
n_dim = 1
x = constant_op.constant([[1.42]])
dy = constant_op.constant([[2.42]])

ta = tensor_array_ops.TensorArray(
    dtypes.float32, size=n_time, element_shape=[n_dim])
for t in range(n_time):
    ta = ta.write(index=t, value=x[t])
    y = ta.stack()
    # dy is outside of the gradients name scope; tf.gradients must
    # wrap it in the correct name scope.
    dx, = gradients_impl.gradients(ys=[y], xs=[x], grad_ys=[dy])
    with self.cached_session():
        vdx, vdy = self.evaluate([dx, dy])
    self.assertAllClose(vdx, vdy)
