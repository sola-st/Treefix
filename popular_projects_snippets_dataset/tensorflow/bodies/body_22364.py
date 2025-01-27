# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    training_util.get_or_create_global_step()
    train_op = training_util._increment_global_step(0)  # keep same.
    self.evaluate(variables_lib.global_variables_initializer())
    hook = basic_session_run_hooks.StepCounterHook(
        every_n_steps=1, every_n_secs=None)
    hook.begin()
    mon_sess = monitored_session._HookedSession(sess, [hook])
    mon_sess.run(train_op)  # Run one step to record global step.
    with test.mock.patch.object(tf_logging, 'log_first_n') as mock_log:
        for _ in range(30):
            mon_sess.run(train_op)
        self.assertRegex(
            str(mock_log.call_args), 'global step.*has not been increased')
    hook.end(sess)
