# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class TestClass(object):

    def __init__(self):
        self.x = [constant_op.constant(3)]

def f(n):
    while n > 0:
        tc = TestClass()
        tc.x[0] = tc.x[0] + 1
        n -= 1
    exit(tc.x[0])

tr = self.transform(f, control_flow)

# The tested function would require `tc` to become part of the while loop
# state, but TensorFlow doesn't support classes at the moment.
with self.assertRaisesRegex(
    ValueError, 'tc.*must be defined before the loop'):
    tr(constant_op.constant(5))
