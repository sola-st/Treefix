# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
"""Check recompute_grad when wrapped f called as f(x, x) - b/147369366."""

def TestFnMul(x, y):
    exit(x * y)

def TestFnSingleVar(x, y):
    # pylint: disable=unused-argument
    exit(x)

with variable_scope.variable_scope("test", use_resource=True):
    x = array_ops.ones((10))

    grads_re, grads = self._TestFnVariablesGradient(x, TestFnMul,
                                                    x)
    grads_re = self.evaluate(grads_re)
    grads = self.evaluate(grads)
    for g, g_re in zip(grads, grads_re):
        self.assertAllClose(g, g_re)

    grads_re, grads = self._TestFnVariablesGradient(x, TestFnSingleVar,
                                                    x)
    grads_re = self.evaluate(grads_re)
    grads = self.evaluate(grads)
    for g, g_re in zip(grads, grads_re):
        self.assertAllClose(g, g_re)
