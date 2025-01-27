# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
try:
    stub = metrics.TFLiteMetrics()
    stub.increase_counter_debugger_creation()
    self.assertEqual(metrics._counter_debugger_creation.get_cell().value(), 1)
    stub2 = metrics.TFLiteMetrics()
    stub2.increase_counter_debugger_creation()
    self.assertEqual(metrics._counter_debugger_creation.get_cell().value(), 2)
    del stub
    gc.collect()
    stub2.increase_counter_debugger_creation()
    self.assertEqual(metrics._counter_debugger_creation.get_cell().value(), 3)
except:
    raise Exception('No exception should be raised.')
