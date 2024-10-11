# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
inputs = np.random.random_sample(input_shape)
sort_inputs = np.sort(inputs)
for n in range(input_shape[-1]):
    expected_values = sort_inputs[..., n]
    self._validateNthElement(
        inputs, dtypes.float32, n, False, expected_values)
    expected_values = sort_inputs[..., ::-1][..., n]
    self._validateNthElement(
        inputs, dtypes.float64, n, True, expected_values)
