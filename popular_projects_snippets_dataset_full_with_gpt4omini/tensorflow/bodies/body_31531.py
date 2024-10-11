# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [
    57157, 63298, 39249, 44026, 9971, 11402, 31193, 36306, 19126, 22948,
    3970, 5060, 5135, 6350, 2666, 3524, 461, 674
]
tensor_in_sizes = [1, 3, 3, 2]
filter_in_sizes = [2, 2, 2, 2]
bias_in_sizes = [2]

x = self._CreateNumpyTensor(tensor_in_sizes)
filter_in = self._CreateNumpyTensor(filter_in_sizes)
bias_in = self._CreateNumpyTensor(bias_in_sizes)

conv1 = self._CreateConv2D(x, filter_in)

conv = self._CreateConv2D(conv1, filter_in)
bias_add = nn_ops.bias_add(conv, bias_in)
add = math_ops.add_n([bias_add, conv1])

self.assertAllEqual(
    np.rint(expected_output),
    self.evaluate(add).reshape(-1))
