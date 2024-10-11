# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
for col, expected_values in cols_to_expected_values.items():
    for i, var in enumerate(cols_to_vars[col]):
        self.assertAllClose(expected_values[i], var.eval(sess))
