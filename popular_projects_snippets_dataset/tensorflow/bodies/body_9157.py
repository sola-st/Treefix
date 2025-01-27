# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'dump')

opts = (
    builder(builder.trainable_variables_parameter()).with_file_output(
        outfile).with_accounted_types(
            ['.*']).with_min_occurrence(10).order_by('occurrence').select([
                'params', 'micros', 'bytes', 'peak_bytes', 'residual_bytes',
                'output_bytes', 'occurrence', 'input_shapes'
            ]).build())

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildFullModel()

    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta, cmd='op', options=opts)

    with gfile.Open(outfile, 'r') as f:
        # pylint: disable=line-too-long
        self.assertEqual(
            'nodename|requestedbytes|peakbytes|residualbytes|outputbytes|totalexecutiontime|acceleratorexecutiontime|cpuexecutiontime|#parameters|opoccurrence(run|defined)|inputshapes',
            lib.CheckAndRemoveDoc(f.read()).replace('\t',
                                                    '').replace(' ', '')[0:170])
        # pylint: enable=line-too-long

    total_children = 0
    last_occurrence = 1e32
    input_shapes = 0
    last_total_micros = tfprof_node.total_exec_micros
    last_micros = tfprof_node.exec_micros
    while tfprof_node.children:
        for gnode in tfprof_node.graph_nodes:
            input_shapes += len(gnode.input_shapes)
        self.assertEqual(len(tfprof_node.children), 1)
        tfprof_node = tfprof_node.children[0]

        self.assertEqual(last_total_micros,
                         tfprof_node.total_exec_micros + last_micros)
        last_total_micros = tfprof_node.total_exec_micros
        last_micros = tfprof_node.exec_micros

        total_children += 1
        self.assertLessEqual(len(tfprof_node.graph_nodes), last_occurrence)
        last_occurrence = len(tfprof_node.graph_nodes)

    self.assertGreater(input_shapes, 0)
