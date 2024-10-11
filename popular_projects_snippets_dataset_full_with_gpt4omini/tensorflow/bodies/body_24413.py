# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
"""Watch output slots on Variable-updating ops, with no emitted edges."""

with session.Session(config=no_rewrite_session_config()) as sess:
    u_init = constant_op.constant(10.0)
    u = variables.VariableV1(u_init, name="gdo/u")
    v_init = constant_op.constant(20.0)
    v = variables.VariableV1(v_init, name="gdo/v")

    w = math_ops.multiply(u, v, name="gdo/w")
    # gdo stands for GradientDescentOptimizer.

    train_op = gradient_descent.GradientDescentOptimizer(
        learning_rate=0.1).minimize(
            w, name="gdo/train")

    u.initializer.run()
    v.initializer.run()

    _, dump = self._debug_run_and_get_dump(sess, train_op)

    update_u_data = dump.watch_key_to_data(
        "gdo/train/update_gdo/u/ApplyGradientDescent:0:DebugIdentity")
    self.assertEqual(1, len(update_u_data))

    # Gradient descent on u: w = u * v, so dw / du = v.
    # Updated value of u should be:
    #   10.0 - learning_rate * v = 10.0 - 0.1 * 20.0 = 8.0
    self.assertAllClose(8.0, update_u_data[0].get_tensor())

    update_v_data = dump.watch_key_to_data(
        "gdo/train/update_gdo/v/ApplyGradientDescent:0:DebugIdentity")
    self.assertEqual(1, len(update_v_data))

    # Gradient descent on u: w = u * v, so dw / dv = u.
    # Updated value of u should be:
    #   20.0 - learning_rate * u = 20.0 - 0.1 * 10.0 = 19.0
    self.assertAllClose(19.0, update_v_data[0].get_tensor())

    # Verify that the Variables u and v are updated properly.
    self.assertAllClose(8.0, sess.run(u))
    self.assertAllClose(19.0, sess.run(v))
