# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_test.py
ops.reset_default_graph()
opts = builder.time_and_memory(min_bytes=0)

with session.Session() as sess:
    r1, r2, r3 = lib.BuildSplittableModel()
    sess.run(variables.global_variables_initializer())

    profiler = model_analyzer.Profiler(sess.graph)
    pb0 = profiler.profile_name_scope(opts)

    run_meta = config_pb2.RunMetadata()
    _ = sess.run(r1,
                 options=config_pb2.RunOptions(
                     trace_level=config_pb2.RunOptions.FULL_TRACE),
                 run_metadata=run_meta)
    profiler.add_step(1, run_meta)
    pb1 = profiler.profile_name_scope(opts)

    self.assertNotEqual(lib.SearchTFProfNode(pb1, 'DW'), None)
    self.assertEqual(lib.SearchTFProfNode(pb1, 'DW2'), None)
    self.assertEqual(lib.SearchTFProfNode(pb1, 'add'), None)

    run_meta2 = config_pb2.RunMetadata()
    _ = sess.run(r2,
                 options=config_pb2.RunOptions(
                     trace_level=config_pb2.RunOptions.FULL_TRACE),
                 run_metadata=run_meta2)
    profiler.add_step(2, run_meta2)
    pb2 = profiler.profile_name_scope(opts)

    self.assertNotEqual(lib.SearchTFProfNode(pb2, 'DW'), None)
    self.assertNotEqual(lib.SearchTFProfNode(pb2, 'DW2'), None)
    self.assertEqual(lib.SearchTFProfNode(pb2, 'add'), None)

    run_meta3 = config_pb2.RunMetadata()
    _ = sess.run(r3,
                 options=config_pb2.RunOptions(
                     trace_level=config_pb2.RunOptions.FULL_TRACE),
                 run_metadata=run_meta3)
    profiler.add_step(3, run_meta3)
    pb3 = profiler.profile_name_scope(opts)

    self.assertNotEqual(lib.SearchTFProfNode(pb3, 'DW'), None)
    self.assertNotEqual(lib.SearchTFProfNode(pb3, 'DW2'), None)
    self.assertNotEqual(lib.SearchTFProfNode(pb3, 'add'), None)

    self.assertEqual(lib.SearchTFProfNode(pb0, 'Conv2D'), None)
    self.assertGreater(lib.SearchTFProfNode(pb1, 'Conv2D').exec_micros, 0)
    self.assertEqual(lib.SearchTFProfNode(pb1, 'Conv2D_1'), None)
    self.assertGreater(lib.SearchTFProfNode(pb2, 'Conv2D_1').exec_micros, 0)
    self.assertEqual(lib.SearchTFProfNode(pb2, 'add'), None)
    self.assertGreater(lib.SearchTFProfNode(pb3, 'add').exec_micros, 0)

    advice_pb = profiler.advise(model_analyzer.ALL_ADVICE)
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
