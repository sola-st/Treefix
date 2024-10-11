# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default() as g, session_lib.Session() as sess:
    with variable_scope.variable_scope('bar'):
        variable_scope.get_variable(
            'foo',
            initializer=0,
            trainable=False,
            collections=[
                ops.GraphKeys.GLOBAL_STEP, ops.GraphKeys.GLOBAL_VARIABLES
            ])
    train_op = training_util._increment_global_step(1)
    summary_writer = fake_summary_writer.FakeSummaryWriter(self.log_dir, g)
    hook = basic_session_run_hooks.StepCounterHook(
        summary_writer=summary_writer, every_n_steps=1, every_n_secs=None)

    hook.begin()
    self.evaluate(variables_lib.global_variables_initializer())
    mon_sess = monitored_session._HookedSession(sess, [hook])
    mon_sess.run(train_op)
    mon_sess.run(train_op)
    hook.end(sess)

    summary_writer.assert_summaries(
        test_case=self,
        expected_logdir=self.log_dir,
        expected_graph=g,
        expected_summaries={})
    self.assertTrue(summary_writer.summaries, 'No summaries were created.')
    self.assertItemsEqual([2], summary_writer.summaries.keys())
    summary_value = summary_writer.summaries[2][0].value[0]
    self.assertEqual('bar/foo/sec', summary_value.tag)
