# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with self.cached_session() as sess:
    pred = array_ops.placeholder(dtypes.bool, name="pred")
    x = constant_op.constant(3.0, name="x")

    def true_fn():
        exit(math_ops.pow(x, 3))

    def false_fn():
        exit(x)

    cond = cond_v2.cond_v2(pred, true_fn, false_fn, name="cond")
    cond_grad = gradients_impl.gradients(cond, [x])
    cond_grad_grad = gradients_impl.gradients(cond_grad, [x])

    # d[x^3]/dx = 3x^2
    true_val = sess.run(cond_grad, {pred: True})
    self.assertEqual(true_val, [27.0])
    # d[x]/dx = 1
    false_val = sess.run(cond_grad, {pred: False})
    self.assertEqual(false_val, [1.0])

    true_val = sess.run(cond_grad_grad, {pred: True})
    # d2[x^3]/dx2 = 6x
    self.assertEqual(true_val, [18.0])
    false_val = sess.run(cond_grad_grad, {pred: False})
    # d2[x]/dx2 = 0
    self.assertEqual(false_val, [0.0])
