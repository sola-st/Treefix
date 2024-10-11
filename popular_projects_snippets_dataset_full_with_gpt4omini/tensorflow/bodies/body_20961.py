# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
strategy = collective_all_reduce_strategy.CollectiveAllReduceStrategy()
strategy.extended._is_chief = False

context = distribute_coordinator._WorkerContext(strategy, None, 'worker', 1)

logdir = _test_dir(self.get_temp_dir(), 'test_save_checkpoint_disabled')
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    new_gstep = state_ops.assign_add(gstep, 1)
    with context, monitored_session.MonitoredTrainingSession(
        checkpoint_dir=logdir,
        save_checkpoint_steps=100,
        log_step_count_steps=10) as session:
        for _ in range(100):
            session.run(new_gstep)

    # No checkpoint is saved.
checkpoint = checkpoint_management.latest_checkpoint(logdir)
self.assertIsNone(checkpoint)

# But saved to a temporary directory.
checkpoint = checkpoint_management.latest_checkpoint(
    os.path.join(logdir, 'tmp_worker_1'))
self.assertIsNotNone(checkpoint)
