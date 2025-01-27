# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
self._assert_iterator_values(iterator, expected_values, evaluate,
                             devices)

with self.assertRaises(errors.OutOfRangeError):
    self._assert_iterator_values(iterator, expected_values, evaluate,
                                 devices)

# After re-initializing the iterator, should be able to iterate again.
if not ops.executing_eagerly_outside_functions():
    evaluate(control_flow_ops.group(iterator.initializer))
else:
    if api_type == "wrap_into_iterator":
        self.skipTest("unsupported test combination")
    else:
        iterator = iter(dataset)

self._assert_iterator_values(iterator, expected_values, evaluate,
                             devices)
