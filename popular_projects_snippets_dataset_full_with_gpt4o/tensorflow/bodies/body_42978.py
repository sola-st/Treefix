# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils_test.py
trace_line_count = -1
if filtering_enabled:
    traceback_utils.enable_traceback_filtering()
else:
    traceback_utils.disable_traceback_filtering()
self.assertEqual(
    traceback_utils.is_traceback_filtering_enabled(), filtering_enabled)
try:
    fn()
except Exception as e:  # pylint: disable=broad-except
    # We must count lines rather than frames because autograph transforms
    # stack frames into a single large string
    trace = '\n'.join(traceback.format_tb(e.__traceback__))
    trace_line_count = len(trace.split('\n'))

self.assertGreater(trace_line_count, 0)

if filtering_enabled:
    self.assertLess(trace_line_count, count)
else:
    self.assertGreater(trace_line_count, count)
