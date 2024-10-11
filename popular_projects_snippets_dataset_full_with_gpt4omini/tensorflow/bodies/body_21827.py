# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
# Create a checkpoint.
checkpoint_dir = os.path.join(
    self.get_temp_dir(),
    "recover_session_ready_for_local_init_fails_stil_run")
try:
    gfile.DeleteRecursively(checkpoint_dir)
except errors.OpError:
    pass  # Ignore
gfile.MakeDirs(checkpoint_dir)

# Create a new Graph and SessionManager and recover.
with ops.Graph().as_default():
    v = variables.VariableV1(2, name="v")
    w = variables.VariableV1(
        1,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="w")
    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
        self.assertEqual(False, variables.is_variable_initialized(w).eval())
    sm2 = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables(),
        ready_for_local_init_op=None,
        local_init_op=w.initializer)
    saver = saver_lib.Saver({"v": v})
    sess, initialized = sm2.recover_session(
        "",
        saver=saver,
        checkpoint_dir=checkpoint_dir,
        wait_for_checkpoint=False)
    self.assertFalse(initialized)
    self.assertEqual(
        False,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v:0")).eval(session=sess))
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("w:0")).eval(session=sess))
    self.assertEqual(1, sess.run(w))
