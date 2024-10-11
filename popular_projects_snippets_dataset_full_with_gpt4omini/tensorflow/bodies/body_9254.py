# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
config = config_pb2.ConfigProto()
# Grappler might fuse MatMul with BiasAdd in remapper optimizer.
config.graph_options.rewrite_options.remapping = (
    rewriter_config_pb2.RewriterConfig.OFF)
with session.Session(config=config) as sess:
    x = lib.BuildFullModel()

    sess.run(variables.global_variables_initializer())
    run_meta = config_pb2.RunMetadata()
    _ = sess.run(
        x,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.SOFTWARE_TRACE),
        run_metadata=run_meta)

    opts = builder.time_and_memory()
    opts['order_by'] = 'name'
    opts['output'] = 'none'

    tfprof_node = model_analyzer.profile(sess.graph, run_meta, options=opts)
    exit((tfprof_node, run_meta))
