# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
# This test checks for backwards compatibility.
# In particular, we continue to ensure that recover_session will execute
# local_init_op exactly once, regardless of whether the session was
# successfully recovered.
with ops.Graph().as_default():
    w = variables.VariableV1(
        1,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="w")
    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(w).eval())
    sm2 = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables(),
        ready_for_local_init_op=None,
        local_init_op=w.initializer)
    # Try to recover session from None
    sess, initialized = sm2.recover_session(
        "", saver=None, checkpoint_dir=None)
    # Succeeds because recover_session still run local_init_op
    self.assertFalse(initialized)
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("w:0")).eval(session=sess))
    self.assertEqual(1, sess.run(w))
