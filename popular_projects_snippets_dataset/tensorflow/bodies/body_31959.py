# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
tensor_in_sizes = [1, 1, 1, 1, 1]
x1 = self._CreateNumpyTensor(tensor_in_sizes)
filter_in = np.ones((1, 1, 0, 1, 1), dtype=np.float32)
with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError, "filter must not have zero elements"
    "|has a non-positive dimension"):
    self.evaluate(
        nn_ops.conv3d(x1, filter_in, strides=[1, 1, 1, 1, 1], padding="SAME"))
