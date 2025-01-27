# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default():
    p = array_ops.placeholder(dtypes.float32, shape=(3,))
    v = variables.VariableV1(p, name="v")
    sm = session_manager.SessionManager(
        ready_op=variables.assert_variables_initialized())
    sess = sm.prepare_session(
        "",
        init_op=variables.global_variables_initializer(),
        init_feed_dict={p: [1.0, 2.0, 3.0]})
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
