# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()

def check_min(nodes, mm=0, mam=0, mcm=0, mb=0, mpb=0, mrb=0, mob=0):
    for n in nodes:
        if mm > 0:
            self.assertGreaterEqual(n.exec_micros, mm)
        if mam > 0:
            self.assertGreaterEqual(n.accelerator_exec_micros, mam)
        if mcm > 0:
            self.assertGreaterEqual(n.cpu_exec_micros, mcm)
        if mb > 0:
            self.assertGreaterEqual(n.requested_bytes, mb)
        if mpb > 0:
            self.assertGreaterEqual(n.peak_bytes, mpb)
        if mrb > 0:
            self.assertGreaterEqual(n.residual_bytes, mrb)
        if mob > 0:
            self.assertGreaterEqual(n.output_bytes, mob)
        check_min(n.children, mm, mam, mcm, mb, mpb, mrb, mob)

with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = lib.BuildSmallModel()
    self.evaluate(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata=run_meta)

    min_val = random.randint(0, 10000)

    opts = builder(builder.time_and_memory(
        min_micros=min_val)).with_empty_output().build()
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_meta, options=opts)
    check_min(tfprof_node.children, mm=min_val)

    opts = builder(builder.time_and_memory(
        min_accelerator_micros=min_val)).with_empty_output().build()
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_meta, options=opts)
    check_min(tfprof_node.children, mam=min_val)

    opts = builder(builder.time_and_memory(
        min_cpu_micros=min_val)).with_empty_output().build()
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_meta, options=opts)
    check_min(tfprof_node.children, mcm=min_val)

    opts = builder(builder.time_and_memory(
        min_bytes=min_val)).with_empty_output().build()
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_meta, options=opts)
    check_min(tfprof_node.children, mb=min_val)

    opts = builder(builder.time_and_memory(
        min_peak_bytes=min_val)).with_empty_output().build()
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_meta, options=opts)
    check_min(tfprof_node.children, mpb=min_val)

    opts = builder(builder.time_and_memory(
        min_residual_bytes=min_val)).with_empty_output().build()
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_meta, options=opts)
    check_min(tfprof_node.children, mrb=min_val)

    opts = builder(builder.time_and_memory(
        min_output_bytes=min_val)).with_empty_output().build()
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_meta, options=opts)
    check_min(tfprof_node.children, mob=min_val)
