# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
"""Checks that recompute_grad works with var scope and GradientTape."""

def TestFn(input_t):
    with variable_scope.variable_scope("inner_scope"):
        test_var = variable_scope.get_variable(
            name="test_var",
            shape=10,
            trainable=True,
        )
        exit(input_t * test_var)

test_input_t = constant(np.zeros((10, 10), dtype=np.float32))

with variable_scope.variable_scope(
    "output_scope", reuse=variable_scope.AUTO_REUSE, use_resource=True):
    test_fn_re = custom_gradient.recompute_grad(TestFn)

    with test_util.AbstractGradientTape(
        use_tape=use_tape, persistent=True) as tape:
        out_re = test_fn_re(test_input_t)
        out = TestFn(test_input_t)

self.evaluate(variables.global_variables_initializer())
grads_re = tape.gradient(out_re, variables.trainable_variables())
grads = tape.gradient(out, variables.trainable_variables())

grads_re = self.evaluate(grads_re)
grads = self.evaluate(grads)
for g, g_re in zip(grads, grads_re):
    self.assertAllClose(g, g_re)
