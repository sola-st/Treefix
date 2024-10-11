# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.graph.as_default():
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir, save_steps=2, scaffold=self.scaffold)
    hook.begin()
    self.scaffold.finalize()
    with session_lib.Session() as sess:
        mon_sess = monitored_session._HookedSession(sess, [hook])
        sess.run(self.scaffold.init_op)
        hook.after_create_session(sess, None)
        # Verifies that checkpoint is saved at step 0.
        self.assertEqual(0,
                         checkpoint_utils.load_variable(self.model_dir,
                                                        self.global_step.name))
        # Verifies that no checkpoint is saved after one training step.
        mon_sess.run(self.train_op)
        self.assertEqual(0,
                         checkpoint_utils.load_variable(self.model_dir,
                                                        self.global_step.name))
        # Verifies that checkpoint is saved after save_steps.
        mon_sess.run(self.train_op)
        self.assertEqual(2,
                         checkpoint_utils.load_variable(self.model_dir,
                                                        self.global_step.name))
