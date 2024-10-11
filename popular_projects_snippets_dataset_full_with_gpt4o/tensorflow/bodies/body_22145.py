# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
super(MixedPrecisionTest, self).setUp()
# Enable the tests to be run on pre-Volta GPUs by telling the grappler pass
# to ignore performance and always transform the graph.
self._original_ignore_perf_value = os.getenv(self.IGNORE_PERF_VAR)
os.environ[self.IGNORE_PERF_VAR] = '1'
