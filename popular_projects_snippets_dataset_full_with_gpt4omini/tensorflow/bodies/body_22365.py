# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
training_util.get_or_create_global_step()
self.train_op = training_util._increment_global_step(steps_per_run)
self.summary_writer = fake_summary_writer.FakeSummaryWriter(
    self.log_dir, graph)
self.hook = basic_session_run_hooks.StepCounterHook(
    summary_writer=self.summary_writer, every_n_steps=every_n_steps)
self.hook._set_steps_per_run(steps_per_run)
self.hook.begin()
self.evaluate(variables_lib.global_variables_initializer())
self.mon_sess = monitored_session._HookedSession(sess, [self.hook])
