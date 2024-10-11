# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
tensor_in_sizes_batch = [10, 2, 3, 1, 3]
tensor_in_sizes_expanded_batch = [2, 5, 2, 3, 1, 3]
filter_in_sizes = [1, 1, 1, 3, 3]
filter_in = self._CreateNumpyTensor(filter_in_sizes)
x1 = self._CreateNumpyTensor(tensor_in_sizes_batch)
x2 = x1.reshape(tensor_in_sizes_expanded_batch)
convolver1 = nn_ops.Convolution(
    input_shape=x1.shape,
    filter_shape=filter_in.shape,
    strides=[1, 1, 1],
    padding="VALID")
self.assertEqual(convolver1.num_batch_dims, 1)
convolver2 = nn_ops.Convolution(
    input_shape=x2.shape,
    filter_shape=filter_in.shape,
    strides=[1, 1, 1],
    padding="VALID")
self.assertEqual(convolver2.num_batch_dims, 2)
conv1 = convolver1(x1, filter_in)
conv2 = convolver2(x2, filter_in)
self.assertEqual(conv1.shape, tensor_in_sizes_batch)
self.assertEqual(conv2.shape, tensor_in_sizes_expanded_batch)
self.assertAllClose(conv1, self.evaluate(conv2).reshape(conv1.shape))
