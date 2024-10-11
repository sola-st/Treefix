# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
mock_time.return_value = MOCK_START_TIME
with ops.Graph().as_default() as g, session_lib.Session() as sess:
    training_util.get_or_create_global_step()
    train_op = training_util._increment_global_step(1)
    summary_writer = fake_summary_writer.FakeSummaryWriter(self.log_dir, g)
    hook = basic_session_run_hooks.StepCounterHook(
        summary_writer=summary_writer, every_n_steps=10)
    hook.begin()
    self.evaluate(variables_lib.global_variables_initializer())
    mon_sess = monitored_session._HookedSession(sess, [hook])
    with test.mock.patch.object(tf_logging, 'warning') as mock_log:
        for _ in range(30):
            mock_time.return_value += 0.01
            mon_sess.run(train_op)
        # logging.warning should not be called.
        self.assertIsNone(mock_log.call_args)
    hook.end(sess)
    summary_writer.assert_summaries(
        test_case=self,
        expected_logdir=self.log_dir,
        expected_graph=g,
        expected_summaries={})
    self.assertItemsEqual([11, 21], summary_writer.summaries.keys())
    for step in [11, 21]:
        summary_value = summary_writer.summaries[step][0].value[0]
        self.assertEqual('global_step/sec', summary_value.tag)
        self.assertGreater(summary_value.simple_value, 0)
