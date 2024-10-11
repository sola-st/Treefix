# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
if self._original_ignore_perf_value is not None:
    os.environ[self.IGNORE_PERF_VAR] = self._original_ignore_perf_value
else:
    del os.environ[self.IGNORE_PERF_VAR]
super(AutoMixedPrecisionTest, self).tearDown()
