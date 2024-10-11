# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
inputs = np.random.randint(-1e3, 1e3, input_shape)
n = np.random.randint(input_shape[-1])
sort_inputs = np.sort(inputs)
expected_values = sort_inputs[..., n]
self._validateNthElement(
    inputs, dtypes.int32, n, False, expected_values)
expected_values = sort_inputs[..., ::-1][..., n]
self._validateNthElement(
    inputs, dtypes.int64, n, True, expected_values)
