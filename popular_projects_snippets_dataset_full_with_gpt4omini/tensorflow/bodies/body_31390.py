# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
tensor_in_sizes_batch = [10, 2, 3, 3]
tensor_in_sizes_expanded_batch = [2, 5, 2, 3, 3]
filter_in_sizes = [1, 1, 3, 3]
filter_in = self._CreateNumpyTensor(filter_in_sizes)
x1 = self._CreateNumpyTensor(tensor_in_sizes_batch)
x2 = x1.reshape(tensor_in_sizes_expanded_batch)
conv1 = nn_ops.convolution(
    x1,
    filter_in,
    strides=[1, 1],
    padding="VALID")
conv2 = nn_ops.convolution(
    x2,
    filter_in,
    strides=[1, 1],
    padding="VALID")
self.assertEqual(conv1.shape, tensor_in_sizes_batch)
self.assertEqual(conv2.shape, tensor_in_sizes_expanded_batch)
self.assertAllEqual(
    conv1,
    self.evaluate(conv2).reshape(conv1.shape))
