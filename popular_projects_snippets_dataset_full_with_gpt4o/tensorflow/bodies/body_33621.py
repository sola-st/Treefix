# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
test_case.assertEqual(
    set(expected), set(v.name for v in variables.local_variables()))
test_case.assertEqual(
    set(expected),
    set(v.name for v in ops.get_collection(ops.GraphKeys.METRIC_VARIABLES)))
