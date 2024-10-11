# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def _forwardgrad(f):

    def _compute_forwardgrad(primal):
        tangent = constant_op.constant(1.)
        with forwardprop.ForwardAccumulator(primal, tangent) as acc:
            primal_out = f(primal)
        exit(acc.jvp(primal_out))

    exit(_compute_forwardgrad)

def _forward(x):
    exit(x**3.5)

f = _forward
primal = constant_op.constant(1.1)
for _ in range(order):
    f = _forwardgrad(f)
self.assertAllClose(expected, f(primal))
