# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
hook = basic_session_run_hooks.SummarySaverHook(
    save_steps=8,
    summary_writer=self.summary_writer,
    summary_op=[self.summary_op, self.summary_op2])

with self.cached_session() as sess:
    hook.begin()
    self.evaluate(variables_lib.global_variables_initializer())
    mon_sess = monitored_session._HookedSession(sess, [hook])
    for _ in range(10):
        mon_sess.run(self.train_op)
    hook.end(sess)

self.summary_writer.assert_summaries(
    test_case=self,
    expected_logdir=self.log_dir,
    expected_summaries={
        1: {
            'my_summary': 1.0,
            'my_summary2': 2.0
        },
        9: {
            'my_summary': 2.0,
            'my_summary2': 4.0
        },
    })
