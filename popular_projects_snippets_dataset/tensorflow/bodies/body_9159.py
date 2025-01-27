# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), attribute + '_pprof.pb.gz')
opts = (
    builder(builder.time_and_memory()).select([
        attribute
    ]).with_max_depth(100000).with_node_names(
        trim_name_regexes=['ops.py.*']).with_pprof_output(outfile).build())

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildFullModel()

    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    _ = model_analyzer.profile(sess.graph, run_meta, cmd='code', options=opts)

    if should_fail:
        self.assertFalse(gfile.Exists(outfile))
        exit()

    profile_pb = profile_pb2.Profile()
    with gfile.Open(outfile, 'rb') as f:
        with gzip.GzipFile(fileobj=io.BytesIO(f.read())) as gzipf:
            profile_pb.ParseFromString(gzipf.read())

    self.assertGreater(len(profile_pb.sample), 10)
    self.assertGreater(len(profile_pb.location), 10)
    self.assertGreater(len(profile_pb.function), 10)
    self.assertGreater(len(profile_pb.string_table), 30)

    has_rnn = False
    for s in profile_pb.string_table:
        if s.find('rnn') > 0:
            has_rnn = True
        self.assertFalse(s.startswith('ops.py'))
    self.assertTrue(has_rnn)
