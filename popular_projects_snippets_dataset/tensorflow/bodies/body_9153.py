# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'dump')
# TODO(xpan): Test 'micros'. Since the execution time changes each run,
# it's a bit difficult to test it now.
opts = (
    builder(builder.trainable_variables_parameter()).with_file_output(
        outfile).with_accounted_types(['.*']).with_node_names(
            show_name_regexes=['.*model_analyzer_testlib.*'
                              ]).account_displayed_op_only(False).select([
                                  'bytes', 'params', 'float_ops',
                                  'num_hidden_ops', 'device', 'input_shapes'
                              ]).build())

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildSmallModel()

    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    model_analyzer.profile(sess.graph, run_meta, cmd='code', options=opts)

    with gfile.Open(outfile, 'r') as f:
        # pylint: disable=line-too-long
        self.assertEqual(
            'node name | requested bytes | # parameters | # float_ops | assigned devices | in',
            lib.CheckAndRemoveDoc(f.read())[0:80])
        # pylint: enable=line-too-long
