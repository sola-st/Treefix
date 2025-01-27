# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'dump')

def check_selection(selected, not_selected):
    with gfile.Open(outfile, 'r') as f:
        s = f.read()
        for attr in selected:
            self.assertTrue(s.find(attr) > 0, s)
        for attr in not_selected:
            self.assertFalse(s.find(attr) > 0, s)

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildSmallModel()
    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    opts = builder(
        builder.time_and_memory()).with_file_output(outfile).select(
            ['micros']).build()
    _ = model_analyzer.profile(sess.graph, run_meta=run_meta, options=opts)
    check_selection(['total execution time', 'accelerator execution time'],
                    ['bytes'])

    opts = builder(
        builder.time_and_memory()).with_file_output(outfile).select(
            ['bytes']).build()
    _ = model_analyzer.profile(sess.graph, run_meta=run_meta, options=opts)
    check_selection(['requested bytes'],
                    ['peak bytes', 'residual bytes', 'output bytes'])

    opts = builder(
        builder.time_and_memory()).with_file_output(outfile).select(
            ['peak_bytes', 'residual_bytes', 'output_bytes']).build()
    _ = model_analyzer.profile(sess.graph, run_meta=run_meta, options=opts)
    check_selection(['peak bytes', 'residual bytes', 'output bytes'],
                    ['requested_bytes'])
