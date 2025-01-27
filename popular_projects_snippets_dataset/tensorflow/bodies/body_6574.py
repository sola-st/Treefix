# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
self._assert_iterator_values(
    iterator,
    expected_values,
    evaluate,
    devices,
    enable_get_next_as_optional=True)

next_element = iterator.get_next_as_optional()
self.assertFalse(self.evaluate(next_element.has_value()))
with self.assertRaises(errors.InvalidArgumentError):
    self._assert_iterator_values(
        iterator, [0],
        evaluate,
        devices,
        enable_get_next_as_optional=True)
