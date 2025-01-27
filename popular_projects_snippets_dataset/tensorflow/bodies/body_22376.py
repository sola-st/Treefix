# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
mock_time.return_value = MOCK_START_TIME
hook = basic_session_run_hooks.SummarySaverHook(
    save_secs=0.5,
    summary_writer=self.summary_writer,
    summary_op=self.summary_op)

with self.cached_session() as sess:
    hook.begin()
    self.evaluate(variables_lib.global_variables_initializer())
    mon_sess = monitored_session._HookedSession(sess, [hook])
    for _ in range(4):
        mon_sess.run(self.train_op)
        mock_time.return_value += 0.5
    hook.end(sess)

self.summary_writer.assert_summaries(
    test_case=self,
    expected_logdir=self.log_dir,
    expected_summaries={
        1: {
            'my_summary': 1.0
        },
        2: {
            'my_summary': 2.0
        },
        3: {
            'my_summary': 3.0
        },
        4: {
            'my_summary': 4.0
        },
    })
