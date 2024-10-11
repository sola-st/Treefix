# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
stub = metrics.TFLiteMetrics()
stub.increase_counter_interpreter_creation()
self.assertEqual(
    metrics._counter_interpreter_creation.get_cell('python').value(), 1)
