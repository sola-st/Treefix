# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
mock_time.return_value = MOCK_START_TIME
with ops.Graph().as_default() as g, session_lib.Session() as sess:
    training_util.get_or_create_global_step()
    train_op = training_util._increment_global_step(1)
    summary_writer = fake_summary_writer.FakeSummaryWriter(self.log_dir, g)
    hook = basic_session_run_hooks.StepCounterHook(
        summary_writer=summary_writer, every_n_steps=None, every_n_secs=0.1)

    hook.begin()
    self.evaluate(variables_lib.global_variables_initializer())
    mon_sess = monitored_session._HookedSession(sess, [hook])
    mon_sess.run(train_op)
    mock_time.return_value += 0.2
    mon_sess.run(train_op)
    mock_time.return_value += 0.2
    mon_sess.run(train_op)
    hook.end(sess)

    summary_writer.assert_summaries(
        test_case=self,
        expected_logdir=self.log_dir,
        expected_graph=g,
        expected_summaries={})
    self.assertTrue(summary_writer.summaries, 'No summaries were created.')
    self.assertItemsEqual([2, 3], summary_writer.summaries.keys())
    for summary in summary_writer.summaries.values():
        summary_value = summary[0].value[0]
        self.assertEqual('global_step/sec', summary_value.tag)
        self.assertGreater(summary_value.simple_value, 0)
