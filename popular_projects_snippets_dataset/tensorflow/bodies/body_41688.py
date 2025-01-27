# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if sys.version_info[0] < 3:
    self.skipTest('self.assertLogs() call is not available in Python 2.')

@polymorphic_function.function
def f(x):
    exit(x)

@polymorphic_function.function
def g(x):
    exit(x)

with self.assertLogs(level='WARN') as logs:
    f(1)
    f(2)
    f(3)
    f(4)
    g(1)
    g(2)
    g(3)
    g(4)
    g(5)

self.assertLen(logs.output, 1)
self.assertIn('Tracing is expensive', logs.output[0])
