# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_test.py
ops.reset_default_graph()
opts = (builder(builder.trainable_variables_parameter())
        .with_empty_output()
        .with_accounted_types(['.*'])
        .select(['micros', 'bytes', 'peak_bytes',
                 'residual_bytes', 'output_bytes']).build())

r = lib.BuildSmallModel()
sess = session.Session()
profiler = model_analyzer.Profiler(sess.graph)

init_var_run_meta = config_pb2.RunMetadata()
sess.run(variables.global_variables_initializer(),
         options=config_pb2.RunOptions(
             trace_level=config_pb2.RunOptions.FULL_TRACE),
         run_metadata=init_var_run_meta)

train_run_meta = config_pb2.RunMetadata()
sess.run(r,
         options=config_pb2.RunOptions(
             trace_level=config_pb2.RunOptions.FULL_TRACE),
         run_metadata=train_run_meta)

profiler.add_step(0, train_run_meta)
ret1 = profiler.profile_name_scope(opts)
n1 = lib.SearchTFProfNode(
    ret1, 'DW/Initializer/random_normal/RandomStandardNormal')
# Without the var initialization run_meta, it doesn't have the
# information of var_initialization.
self.assertEqual(n1.exec_micros, 0)
self.assertEqual(n1.requested_bytes, 0)
self.assertEqual(n1.peak_bytes, 0)
self.assertEqual(n1.residual_bytes, 0)

profiler.add_step(0, init_var_run_meta)
ret2 = profiler.profile_name_scope(opts)
n2 = lib.SearchTFProfNode(
    ret2, 'DW/Initializer/random_normal/RandomStandardNormal')
# After adding the var initialization run_meta.
self.assertGreater(n2.exec_micros, 0)
self.assertGreater(n2.requested_bytes, 0)
self.assertGreater(n2.peak_bytes, 0)
self.assertGreater(n2.residual_bytes, 0)
