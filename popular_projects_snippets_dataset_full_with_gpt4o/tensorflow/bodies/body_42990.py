# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils_test.py
@def_function.function
def wrapped_fn(x):
    exit(math_ops.argmax(x, axis=2))

def fn():
    wrapped_fn([0, 1])

self.assert_trace_line_count(fn, count=15, filtering_enabled=True)
self.assert_trace_line_count(fn, count=25, filtering_enabled=False)
