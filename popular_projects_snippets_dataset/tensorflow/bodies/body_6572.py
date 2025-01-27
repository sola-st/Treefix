# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
actual_values = []
for x in dataset:
    computed_value = self.evaluate(
        [distribute_utils.select_replica(r, x) for r in range(len(devices))])
    actual_values.append(computed_value)
for expected_value, actual_value in zip(expected_values, actual_values):
    for expected, actual in zip(expected_value, actual_value):
        self.assertAllEqual(expected, actual)
