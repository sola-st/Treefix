# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
x = random_ops.random_normal(shape=[1, SIZE])
w = random_ops.random_normal(shape=[SIZE, 2 * SIZE])
y = math_ops.matmul(x, w)

config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.arithmetic_optimization = (
    rewriter_config_pb2.RewriterConfig.OFF)
with session.Session(config=config) as sess:
    run_metadata = config_pb2.RunMetadata()
    opts = builder.time_and_memory()
    opts['min_micros'] = 0
    opts['min_bytes'] = 0
    opts['order_by'] = 'name'
    opts['output'] = 'none'
    _ = sess.run(
        y,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.SOFTWARE_TRACE),
        run_metadata=run_metadata)
    tfprof_node = model_analyzer.profile(
        sess.graph, run_meta=run_metadata, options=opts)

    exit((tfprof_node, run_metadata))
