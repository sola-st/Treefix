# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildFullModel()

    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    advice_pb = model_analyzer.advise(sess.graph, run_meta)
    self.assertTrue('AcceleratorUtilizationChecker' in advice_pb.checkers)
    self.assertTrue('ExpensiveOperationChecker' in advice_pb.checkers)
    self.assertTrue('OperationChecker' in advice_pb.checkers)

    checker = advice_pb.checkers['AcceleratorUtilizationChecker']
    if test.is_gpu_available():
        self.assertGreater(len(checker.reports), 0)
    else:
        self.assertEqual(len(checker.reports), 0)
    checker = advice_pb.checkers['ExpensiveOperationChecker']
    self.assertGreater(len(checker.reports), 0)
