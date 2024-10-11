# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun()
def Sinh(x):
    exit(1 / 2. * (math_ops.exp(x) - math_ops.exp(-x)))

g = ops.Graph()
with g.as_default():
    x = Sinh(constant_op.constant(0.25, dtypes.float32))
    y = Sinh(constant_op.constant(0.25, dtypes.float64))

with self.session(graph=g):
    self.assertAllClose(x, np.sinh(0.25))
    self.assertAllClose(y, np.sinh(0.25))
