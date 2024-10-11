# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
# Create a checkpoint.
checkpoint_dir = os.path.join(self.get_temp_dir(), "recover_session")
try:
    gfile.DeleteRecursively(checkpoint_dir)
except errors.OpError:
    pass  # Ignore
gfile.MakeDirs(checkpoint_dir)

with ops.Graph().as_default():
    v = variables.VariableV1(1, name="v")
    sm = session_manager.SessionManager(
        ready_op=variables.assert_variables_initialized())
    saver = saver_lib.Saver({"v": v})
    sess, initialized = sm.recover_session(
        "", saver=saver, checkpoint_dir=checkpoint_dir)
    self.assertFalse(initialized)
    sess.run(v.initializer)
    self.assertEqual(1, sess.run(v))
    saver.save(sess, os.path.join(checkpoint_dir,
                                  "recover_session_checkpoint"))
# Create a new Graph and SessionManager and recover.
with ops.Graph().as_default():
    v = variables.VariableV1(2, name="v")
    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
    sm2 = session_manager.SessionManager(
        ready_op=variables.assert_variables_initialized())
    saver = saver_lib.Saver({"v": v})
    sess, initialized = sm2.recover_session(
        "", saver=saver, checkpoint_dir=checkpoint_dir)
    self.assertTrue(initialized)
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v:0")).eval(session=sess))
    self.assertEqual(1, sess.run(v))
