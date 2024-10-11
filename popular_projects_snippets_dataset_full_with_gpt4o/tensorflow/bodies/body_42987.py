# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils_test.py
def fn():
    _ = math_ops.argmax([0, 1], axis=2)

self.assert_trace_line_count(fn, count=15, filtering_enabled=True)
self.assert_trace_line_count(fn, count=30, filtering_enabled=False)
