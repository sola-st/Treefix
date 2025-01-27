# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
"""Checks that recompute_grad works grads of function args."""

def TestFn(inputs, input_vars):
    exit(inputs * input_vars)

def TestFnSeq(inputs, input_vars):
    exit((inputs * input_vars, inputs * input_vars * 2.0))

with variable_scope.variable_scope("test", use_resource=True):
    test_var = variable_scope.get_variable(
        name="test_var",
        shape=10,
        trainable=True,
    )
    self.evaluate(test_var.assign(np.ones([10])))
    test_input = constant(np.ones((10, 10), dtype=np.float32))

    grads_re, grads = self._TestFnVariablesGradient(test_input, TestFn,
                                                    test_input)

    grads_re = self.evaluate(grads_re)
    grads = self.evaluate(grads)
    for g, g_re in zip(grads, grads_re):
        self.assertAllClose(g, g_re)

    grads_re, grads = self._TestFnVariablesGradient(test_input, TestFn,
                                                    test_var)
    grads_re = self.evaluate(grads_re)
    grads = self.evaluate(grads)
    for g, g_re in zip(grads, grads_re):
        self.assertAllClose(g, g_re)

    # Regression test for wrapping sequence outputting functions.
    grads_re, grads = self._TestFnVariablesGradient(test_input, TestFnSeq,
                                                    test_input)
    grads_re = self.evaluate(grads_re)
    grads = self.evaluate(grads)
    for g, g_re in zip(grads, grads_re):
        self.assertAllClose(g, g_re)

    grads_re, grads = self._TestFnVariablesGradient(test_input, TestFnSeq,
                                                    test_var)
    grads_re = self.evaluate(grads_re)
    grads = self.evaluate(grads)
    for g, g_re in zip(grads, grads_re):
        self.assertAllClose(g, g_re)
