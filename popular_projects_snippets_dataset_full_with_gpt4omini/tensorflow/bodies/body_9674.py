# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    ph = array_ops.placeholder(dtypes.float32)
    a = math_ops.add(ph, 1.0)
    callable_opts = config_pb2.CallableOptions()
    callable_opts.feed.append(ph.name)
    callable_opts.fetch.append(a.name)
    callable_opts.run_options.trace_level = config_pb2.RunOptions.FULL_TRACE
    callable_fn = sess._make_callable_from_options(callable_opts)
    run_metadata = config_pb2.RunMetadata()
    self.assertEqual([2.0], callable_fn(np.array(1.0, dtype=np.float32),
                                        run_metadata=run_metadata))
    self.assertGreater(len(run_metadata.step_stats.dev_stats), 0)
