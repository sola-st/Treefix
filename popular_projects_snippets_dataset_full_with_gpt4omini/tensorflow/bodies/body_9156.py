# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'timeline')
opts = (
    builder(builder.trainable_variables_parameter()).with_max_depth(100000)
    .with_step(0).with_timeline_output(outfile).with_accounted_types(
        ['.*']).build())

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildFullModel()

    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    _ = model_analyzer.profile(
        sess.graph, run_meta, cmd='graph', options=opts)

    with gfile.Open(outfile + '_0', 'r') as f:
        # Test that a json file is created.
        # TODO(xpan): tfprof Timeline isn't quite correct on Windows.
        # Investigate why.
        if os.name != 'nt':
            self.assertLess(1000, len(f.read()))
        else:
            self.assertLess(1, len(f.read()))
