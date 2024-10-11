# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
logdir = _test_dir(self.get_temp_dir(), 'test_summaries_steps')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    new_gstep = state_ops.assign_add(gstep, 1)
    summary.scalar('my_summary_tag', new_gstep * 2)
    with monitored_session.MonitoredTrainingSession(
        is_chief=True,
        checkpoint_dir=logdir,
        save_summaries_steps=100,
        log_step_count_steps=10) as session:
        for _ in range(101):
            session.run(new_gstep)
summaries = latest_summaries(logdir)
tags = [s.summary.value[0].tag for s in summaries]
self.assertIn('my_summary_tag', tags)
self.assertIn('global_step/sec', tags)
