# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils_test.py

def fn():
    x = array_ops.zeros((2, 3))
    y = array_ops.zeros((2, 4))
    _ = x + y

self.assert_trace_line_count(fn, count=15, filtering_enabled=True)
self.assert_trace_line_count(fn, count=25, filtering_enabled=False)
