# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
# Create a new Graph and SessionManager and recover from a checkpoint.
with ops.Graph().as_default():
    v = variables.VariableV1(2, name="v")
    with session_lib.Session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
    sm2 = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables())
    saver = saver_lib.Saver({"v": v})
    sess, initialized = sm2.recover_session(
        "",
        saver=saver,
        checkpoint_dir=checkpoint_dir,
        checkpoint_filename_with_path=checkpoint_filename_with_path)
    self.assertTrue(initialized)
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v:0")).eval(session=sess))
    self.assertEqual(1, sess.run(v))
