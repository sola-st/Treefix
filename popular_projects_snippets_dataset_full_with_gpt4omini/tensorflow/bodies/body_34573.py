# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=3, dynamic_size=True)
    x = constant_op.constant([1.0, 2.0, 3.0])
    w0 = ta.split(x, [1, 1, 1])
    w1 = w0.write(3, [4.0])
    r = w1.concat()
    self.assertAllEqual(np.array([1.0, 2.0, 3.0, 4.0]), self.evaluate(r))
    grad = gradients_impl.gradients(ys=[r], xs=[x])
    self.assertAllEqual(np.array([1.0, 1.0, 1.0]), self.evaluate(grad)[0])
