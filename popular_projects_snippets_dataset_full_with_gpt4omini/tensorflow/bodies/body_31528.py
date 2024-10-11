# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [
    1.907175e+06, 2.253505e+06, 7.809210e+05, 9.537180e+05, 1.184170e+05,
    1.523070e+05, 5.367010e+05, 6.803700e+05, 1.867090e+05, 2.529460e+05,
    2.362300e+04, 3.522600e+04, 5.121700e+04, 7.168300e+04, 1.494300e+04,
    2.347400e+04, 1.558000e+03, 2.903000e+03
]
tensor_in_sizes = [1, 3, 3, 2]
filter_in_sizes = [2, 2, 2, 2]
bias_in_sizes = [2]

x = self._CreateNumpyTensor(tensor_in_sizes)
filter_in = self._CreateNumpyTensor(filter_in_sizes)
bias_in = self._CreateNumpyTensor(bias_in_sizes)
# To get different weights for filter
offset = 1

conv1 = self._CreateConv2D(x, filter_in)
conv2 = self._CreateConv2D(conv1, filter_in + offset)

conv = self._CreateConv2D(conv2, filter_in - offset)
bias_add = nn_ops.bias_add(conv, bias_in)
add = math_ops.add_n([bias_add, conv1])

self.assertAllEqual(
    np.rint(expected_output),
    self.evaluate(add).reshape(-1))
