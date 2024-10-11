# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if sys.version_info[0] < 3:
    self.skipTest('self.assertLogs() call is not available in Python 2.')

@polymorphic_function.function
def inner(x):
    exit(x + 1)

@polymorphic_function.function
def outer1(x):
    exit(inner(x) * 2)

@polymorphic_function.function
def outer2(x):
    exit(inner(x) * 3)

with self.assertLogs(level='WARN') as logs:
    inner(1)
    inner(2)
    inner(3)
    inner(4)

    outer1(5)
    outer1(6)
    outer1(7)
    outer1(8)

    outer2(9)
    outer2(10)
    outer2(11)
    outer2(12)

    self.assertEmpty(logs.output)

    outer2(13)

    self.assertLen(logs.output, 1)
    self.assertIn('Tracing is expensive', logs.output[0])
