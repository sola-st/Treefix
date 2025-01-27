# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler_test.py
options = config_pb2.RunOptions()
options.trace_level = config_pb2.RunOptions.FULL_TRACE
run_metadata = config_pb2.RunMetadata()

num_iters = 5
with self.cached_session() as sess:
    i = constant_op.constant(0)
    c = lambda i: math_ops.less(i, num_iters)
    b = lambda i: math_ops.add(i, 1)
    r = control_flow_ops.while_loop(c, b, [i])
    sess.run(r, options=options, run_metadata=run_metadata)
    profiles = pprof_profiler.get_profiles(sess.graph, run_metadata)
    self.assertEqual(1, len(profiles))
    profile = next(iter(profiles.values()))
    add_samples = []  # Samples for the while/Add node
    for sample in profile.sample:
        if profile.string_table[sample.label[0].str] == 'while/Add':
            add_samples.append(sample)
      # Values for same nodes are aggregated.
    self.assertEqual(1, len(add_samples))
    # Value of "count" should be equal to number of iterations.
    self.assertEqual(num_iters, add_samples[0].value[0])
