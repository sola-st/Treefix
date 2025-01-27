# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default():
    v = variables.VariableV1([125], name="v")
    sm = session_manager.SessionManager(
        ready_op=variables.assert_variables_initialized())
    sess = sm.prepare_session(
        "", init_fn=lambda sess: sess.run(v.initializer))
    self.assertAllClose([125], sess.run(v))
