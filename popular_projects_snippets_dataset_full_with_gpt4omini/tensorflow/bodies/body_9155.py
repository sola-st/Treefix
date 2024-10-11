# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
opts = (
    builder(builder.trainable_variables_parameter()).with_empty_output()
    .with_accounted_types(['.*']).account_displayed_op_only(False).select(
        ['bytes', 'params', 'float_ops', 'device']).build())

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildSmallModel()

    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta, cmd='code', options=opts)

    leaf = tfprof_node
    while leaf.children:
        self.assertEqual(0, len(leaf.graph_nodes))
        leaf = leaf.children[0]
    self.assertEqual(1, len(leaf.graph_nodes))
