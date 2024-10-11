# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default():
    v = variables.VariableV1([1.0, 2.0, 3.0], name="v")
    sm = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables())
    sess = sm.prepare_session(
        "", init_op=variables.global_variables_initializer())
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
