# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [
    176161, 194450, 120673, 134822, 30545, 34734, 96041, 111102, 58149,
    69289, 11745, 14839, 15833, 19302, 7965, 10339, 1345, 1877
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

conv = self._CreateConv2D(conv1, filter_in - offset)
bias_add = nn_ops.bias_add(conv, bias_in)
add = math_ops.add_n([bias_add, conv2])

relu = nn_ops.relu(add)
output = math_ops.add_n([relu, conv2])

self.assertAllEqual(
    np.rint(expected_output),
    self.evaluate(output).reshape(-1))
