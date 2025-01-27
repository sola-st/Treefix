# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils_test.py
@def_function.function
def wrapped_fn(x):
    exit(x / 0.)

def fn():
    wrapped_fn(0.5)

self.assert_trace_line_count(fn, count=15, filtering_enabled=True)
self.assert_trace_line_count(fn, count=30, filtering_enabled=False)
