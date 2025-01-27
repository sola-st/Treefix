# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.graph.as_default():
    hook = basic_session_run_hooks.CheckpointSaverHook(
        self.model_dir,
        save_steps=2*self.steps_per_run,
        scaffold=self.scaffold)
    hook._set_steps_per_run(self.steps_per_run)
    hook.begin()
    self.scaffold.finalize()
    with session_lib.Session() as sess:
        sess.run(self.scaffold.init_op)
        mon_sess = monitored_session._HookedSession(sess, [hook])
        mon_sess.run(self.train_op)
        self.assertEqual(5,
                         checkpoint_utils.load_variable(self.model_dir,
                                                        self.global_step.name))
