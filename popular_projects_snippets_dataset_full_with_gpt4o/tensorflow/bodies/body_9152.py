# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'dump')
opts = (
    builder(builder.trainable_variables_parameter()).with_file_output(
        outfile).with_accounted_types(['.*']).select([
            'params', 'float_ops', 'occurrence', 'device', 'op_types',
            'input_shapes'
        ]).build())

with session.Session(config=self._no_rewrite_session_config()
                    ) as sess, ops.device('/device:CPU:0'):
    x = lib.BuildSmallModel()

    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    model_analyzer.profile(sess.graph, run_meta, options=opts)
