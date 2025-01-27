# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'dump')
opts = (builder(builder.trainable_variables_parameter())
        .with_file_output(outfile)
        .with_accounted_types(['.*'])
        .select(['params', 'float_ops', 'micros', 'bytes',
                 'device', 'op_types', 'occurrence']).build())

# Test the output without run_meta.
sess = session.Session()
r = lib.BuildFullModel()
sess.run(variables.global_variables_initializer())

# Test the output with run_meta.
run_meta = config_pb2.RunMetadata()
_ = sess.run(r,
             options=config_pb2.RunOptions(
                 trace_level=config_pb2.RunOptions.FULL_TRACE),
             run_metadata=run_meta)

profiler = model_analyzer.Profiler(sess.graph)
profiler.add_step(1, run_meta)
profiler.profile_graph(opts)
with gfile.Open(outfile, 'r') as f:
    profiler_str = f.read()

model_analyzer.profile(
    sess.graph, cmd='graph', run_meta=run_meta, options=opts)
with gfile.Open(outfile, 'r') as f:
    pma_str = f.read()
self.assertEqual(pma_str, profiler_str)

profiler.profile_name_scope(opts)
with gfile.Open(outfile, 'r') as f:
    profiler_str = f.read()

model_analyzer.profile(
    sess.graph, cmd='scope', run_meta=run_meta, options=opts)
with gfile.Open(outfile, 'r') as f:
    pma_str = f.read()
self.assertEqual(pma_str, profiler_str)

profiler.profile_python(opts)
with gfile.Open(outfile, 'r') as f:
    profiler_str = f.read()

model_analyzer.profile(
    sess.graph, cmd='code', run_meta=run_meta, options=opts)
with gfile.Open(outfile, 'r') as f:
    pma_str = f.read()
self.assertEqual(pma_str, profiler_str)

profiler.profile_operations(opts)
with gfile.Open(outfile, 'r') as f:
    profiler_str = f.read()

model_analyzer.profile(
    sess.graph, cmd='op', run_meta=run_meta, options=opts)
with gfile.Open(outfile, 'r') as f:
    pma_str = f.read()
self.assertEqual(pma_str, profiler_str)

model_analyzer.profile(
    sess.graph, cmd='scope', run_meta=run_meta, options=opts)
with gfile.Open(outfile, 'r') as f:
    pma_str = f.read()
self.assertNotEqual(pma_str, profiler_str)
