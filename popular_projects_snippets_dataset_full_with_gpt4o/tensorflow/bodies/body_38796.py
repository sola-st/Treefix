# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/gradient_correctness_test.py
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    x = constant_op.constant(1.0, dtype=dtypes.float32)
    tape.watch(x)

    yexp = math_ops.exp(x)
    yexplog = math_ops.log(yexp)
    grads = tape.gradient([yexp, yexplog], [x])
    grad_vals = self.evaluate(grads)
    exp1_plus_one = (1.0 + np.exp(1.0)).astype(np.float32)
    # [dexp(x)/dx + d(log(exp(x)))/dx] @ x=1 == exp(1) + 1
    self.assertAllClose(grad_vals[0], exp1_plus_one)
