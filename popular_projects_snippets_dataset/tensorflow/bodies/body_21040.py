# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_num_steps')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    do_step = state_ops.assign_add(gstep, 1)
    # Do 3 steps and save.
    hooks = [basic_session_run_hooks.StopAtStepHook(num_steps=3)]
    with monitored_session.MonitoredSession(hooks=hooks) as session:
        session.run(do_step)
        self.assertFalse(session.should_stop())
        session.run(do_step)
        self.assertFalse(session.should_stop())
        session.run(do_step)
        self.assertTrue(session.should_stop())
        save_path = saver_lib._get_saver_or_default().save(
            session._coordinated_creator.tf_sess,
            os.path.join(logdir, 'step-3'))
    # Restore and do 4 steps.
    def load_ckpt(scaffold, sess):
        scaffold.saver.restore(sess, save_path)

    session_creator = monitored_session.ChiefSessionCreator(
        scaffold=monitored_session.Scaffold(init_fn=load_ckpt))
    hooks = [basic_session_run_hooks.StopAtStepHook(num_steps=4)]
    with monitored_session.MonitoredSession(
        hooks=hooks, session_creator=session_creator) as session:
        self.assertEqual(4, session.run(do_step))
        self.assertFalse(session.should_stop())
        session.run(do_step)
        self.assertFalse(session.should_stop())
        session.run(do_step)
        self.assertFalse(session.should_stop())
        session.run(do_step)
        self.assertTrue(session.should_stop())
