# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
mock_time.return_value = MOCK_START_TIME
with ops.Graph().as_default() as g, session_lib.Session() as sess:
    self._setup_steps_per_run_test(5, 10, g, sess)

    # Logs at 20, 30, 40, 50
    for _ in range(5):
        mock_time.return_value += 0.01
        self.mon_sess.run(self.train_op)

    self.hook.end(sess)
    self.summary_writer.assert_summaries(
        test_case=self,
        expected_logdir=self.log_dir,
        expected_graph=g,
        expected_summaries={})
    self.assertItemsEqual([20, 30, 40, 50],
                          self.summary_writer.summaries.keys())
    for step in [20, 30, 40, 50]:
        summary_value = self.summary_writer.summaries[step][0].value[0]
        self.assertEqual('global_step/sec', summary_value.tag)
        self.assertGreater(summary_value.simple_value, 0)
