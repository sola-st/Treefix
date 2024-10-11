# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
a = array_ops.constant(np.ones((100, 100)))
b = array_ops.constant(np.ones((100, 100)))
c = a * b
config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.min_graph_nodes = -1

with session.Session(config=config) as sess:
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()
    sess.run(c, options=run_options, run_metadata=run_metadata)

    options = option_builder.ProfileOptionBuilder.time_and_memory()
    options['min_bytes'] = 0
    options['select'] = ('bytes', 'peak_bytes', 'output_bytes',
                         'residual_bytes')
    ret = model_analyzer.profile(
        sess.graph, run_meta=run_metadata, cmd='scope', options=options)

    run_metadata = config_pb2.RunMetadata()
    sess.run(c, options=run_options, run_metadata=run_metadata)
    ret2 = model_analyzer.profile(
        sess.graph, run_meta=run_metadata, cmd='scope', options=options)

    n = lib.SearchTFProfNode(ret, 'mul')
    n2 = lib.SearchTFProfNode(ret2, 'mul')
    self.assertGreater(n.peak_bytes, 0)
    self.assertGreater(n.output_bytes, 0)
    self.assertGreater(n.residual_bytes, 0)
    self.assertEqual(n.peak_bytes, n2.peak_bytes)
    self.assertEqual(n.output_bytes, n2.output_bytes)
    self.assertEqual(n.residual_bytes, n2.residual_bytes)
