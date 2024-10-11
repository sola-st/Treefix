# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
# Set the IGNORE_PERF_VAR variable back to it's original value.
if self._original_ignore_perf_value is not None:
    os.environ[self.IGNORE_PERF_VAR] = self._original_ignore_perf_value
else:
    del os.environ[self.IGNORE_PERF_VAR]

mixed_precision.disable_mixed_precision_graph_rewrite_v1()
super(MixedPrecisionTest, self).tearDown()
