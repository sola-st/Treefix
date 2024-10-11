# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_save_graph_def')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    new_gstep = state_ops.assign_add(gstep, 1)
    with monitored_session.MonitoredTrainingSession(
        is_chief=True,
        checkpoint_dir=logdir,
        save_checkpoint_steps=1,
        save_graph_def=False) as session:
        self.assertNotIn('graph.pbtxt', os.listdir(logdir))
        self.assertEmpty(glob.glob(os.path.join(logdir, '*.meta')))
        session.run(new_gstep)
        self.assertEmpty(glob.glob(os.path.join(logdir, '*.meta')))
