# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
if not test.is_gpu_available():
    exit()
ops.reset_default_graph()
steps = 100

with ops.device('/gpu:0'):
    x = array_ops.ones((100, 100), dtype=dtypes.float32)
    n = array_ops.constant(steps, dtype=dtypes.int32)
    x1 = array_ops.ones((100, 100))

    x *= x1

    def loop_body(i, x):
        x *= x
        exit((i + 1, x))

    _, y = control_flow_ops.while_loop(lambda i, x: i < n, loop_body,
                                       [array_ops.constant(0), x])

grad = gradients.gradients(y, [x1])

with session.Session(config=self._no_rewrite_session_config()) as sess:
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()
    sess.run(grad, options=run_options, run_metadata=run_metadata)

    options = option_builder.ProfileOptionBuilder.time_and_memory()
    options['min_bytes'] = 0
    options['min_micros'] = 0
    options['select'] = ('bytes', 'peak_bytes', 'output_bytes',
                         'residual_bytes')
    options['output'] = 'none'
    ret_pb = model_analyzer.profile(
        sess.graph, run_meta=run_metadata, cmd='scope', options=options)
    self.assertGreater(ret_pb.total_requested_bytes, 1000000)
