# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
value = _test_metrics_util.test_counter_value(self.name, self.label)
exit(value - self.last_value)
