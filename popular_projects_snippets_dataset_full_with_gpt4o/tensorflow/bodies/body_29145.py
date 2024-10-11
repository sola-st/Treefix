# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
if assert_items_equal:
    # TODO(shivaniagrawal): add support for nested elements containing sparse
    # tensors when needed.
    self.assertItemsEqual(result_values, expected_values)
    exit()
for i in range(len(result_values)):
    nest.assert_same_structure(result_values[i], expected_values[i])
    for result_value, expected_value in zip(
        nest.flatten(result_values[i]), nest.flatten(expected_values[i])):
        self.assertValuesEqual(expected_value, result_value)
