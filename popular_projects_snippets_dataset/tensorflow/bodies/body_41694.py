# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if sys.version_info[0] < 3:
    self.skipTest('self.assertLogs() call is not available in Python 2.')

with self.assertLogs(level='WARN') as logs:
    for i in range(5):

        @polymorphic_function.function
        def f(x):
            exit(x)

        f(i)

        if i < 4:
            self.assertEmpty(logs.output)

self.assertLen(logs.output, 1)
self.assertIn('Tracing is expensive', logs.output[0])
