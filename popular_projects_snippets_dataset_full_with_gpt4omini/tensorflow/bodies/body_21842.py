# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(), "prepare_session")
checkpoint_dir2 = os.path.join(self.get_temp_dir(), "prepare_session2")
try:
    gfile.DeleteRecursively(checkpoint_dir)
    gfile.DeleteRecursively(checkpoint_dir2)
except errors.OpError:
    pass  # Ignore
gfile.MakeDirs(checkpoint_dir)

with ops.Graph().as_default():
    v = variables.VariableV1([1.0, 2.0, 3.0], name="v")
    sm = session_manager.SessionManager(
        ready_op=variables.assert_variables_initialized())
    saver = saver_lib.Saver({"v": v})
    sess = sm.prepare_session(
        "",
        init_op=variables.global_variables_initializer(),
        saver=saver,
        checkpoint_dir=checkpoint_dir)
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
    checkpoint_filename = os.path.join(checkpoint_dir,
                                       "prepare_session_checkpoint")
    saver.save(sess, checkpoint_filename)
# Create a new Graph and SessionManager and recover.
with ops.Graph().as_default():
    # Renames the checkpoint directory.
    os.rename(checkpoint_dir, checkpoint_dir2)
    gfile.MakeDirs(checkpoint_dir)
    v = variables.VariableV1([6.0, 7.0, 8.0], name="v")
    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
    session_manager.SessionManager(
        ready_op=variables.assert_variables_initialized())
    saver = saver_lib.Saver({"v": v})
    # This should fail as there's no checkpoint within 2 seconds.
    with self.assertRaisesRegex(
        RuntimeError, "no init_op or init_fn or local_init_op was given"):
        sess = sm.prepare_session(
            "",
            init_op=None,
            saver=saver,
            checkpoint_dir=checkpoint_dir,
            wait_for_checkpoint=True,
            max_wait_secs=2)
    # Rename the checkpoint directory back.
    gfile.DeleteRecursively(checkpoint_dir)
    os.rename(checkpoint_dir2, checkpoint_dir)
    # This should succeed as there's checkpoint.
    sess = sm.prepare_session(
        "",
        init_op=None,
        saver=saver,
        checkpoint_dir=checkpoint_dir,
        wait_for_checkpoint=True,
        max_wait_secs=2)
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v:0")).eval(session=sess))
