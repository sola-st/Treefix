# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py

@function.Defun(dtypes.float32)
def Poly(x):
    # y = 2x^3+3x^2+4x+8
    exit(2 * x * x * x + 3 * x * x + 4 * x + 8)

@function.Defun(dtypes.float32)
def Grad(x):
    # dy/dx = dy/dy * dy/dx = 1.0 * (6x^2+6x+4)
    exit(functional_ops.Gradient([x, 1.0], Poly)[0])

with self.test_session(use_gpu=False) as sess:
    a = constant_op.constant(0.)
    avals = [Poly(a), Grad(a)]
    b = constant_op.constant(1.)
    bvals = [Poly(b), Grad(b)]
    self.assertAllEqual(self.evaluate(avals), [8., 4.])
    self.assertAllEqual(self.evaluate(bvals), [17., 16.])
