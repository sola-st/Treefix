# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
actual_values = []
for _ in range(len(expected_values)):
    if enable_get_next_as_optional:
        next_element = iterator.get_next_as_optional().get_value()
    else:
        next_element = iterator.get_next()
    computed_value = evaluate_fn([
        distribute_utils.select_replica(r, next_element)
        for r in range(len(devices))
    ])
    actual_values.append(computed_value)
for expected_value, actual_value in zip(expected_values, actual_values):
    for expected, actual in zip(expected_value, actual_value):
        self.assertAllEqual(expected, actual)
