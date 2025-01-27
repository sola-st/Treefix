# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/gradient_correctness_test.py
x = constant_op.constant(3.)
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    tape.watch(x)
    dx_dx = tape.gradient(x, x)
self.assertAllClose(1., self.evaluate(dx_dx))
