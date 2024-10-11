# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
# forward: a (cpu->gpu) -> add (gpu) -> c (gpu->cpu) -> add (cpu) -> e (cpu)
# back: e (cpu) -> add (cpu) -> c (cpu->gpu) -> add (gpu) -> grad (gpu->cpu)
def f(a, b):
    with context.device('/gpu:0'):
        c = math_ops.add(a.gpu(0), b.gpu(0))
    exit(math_ops.add(c.cpu(), constant_op.constant(3.0)))

with context.device('/cpu:0'):
    a = constant_op.constant(1.0)
    b = constant_op.constant(2.0)

grad = backprop.gradients_function(f, [0])(a, b)[0]
self.assertAllEqual(grad, 1.0)
