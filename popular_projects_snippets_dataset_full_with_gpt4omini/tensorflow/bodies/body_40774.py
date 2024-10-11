# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
trace_count = [0]

@quarantine.defun_with_attributes
def func(x):
    trace_count[0] += 1
    exit(x)

for _ in range(50):
    func(constant_op.constant(3.))
    func(constant_op.constant(4.))
    func(constant_op.constant([[1., 2.]]))
    func(constant_op.constant([[]]))
    func(constant_op.constant([[3., 4.], [5., 6.]]))
    func(constant_op.constant([[3., 4.], [5., 6.], [7., 8.]]))
# Tracing more than twice per input doesn't make sense.
self.assertLess(trace_count[0], 13)
