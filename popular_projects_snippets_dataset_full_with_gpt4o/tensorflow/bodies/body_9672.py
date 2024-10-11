# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    ph = array_ops.placeholder(dtypes.float32)
    a = math_ops.add(ph, 1.0)
    tensor_runner = sess.make_callable(
        a, feed_list=[ph.name], accept_options=True)
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()
    self.assertEqual(0, len(run_metadata.step_stats.dev_stats))
    self.assertAllClose(42.0,
                        tensor_runner(
                            41.0,
                            options=run_options,
                            run_metadata=run_metadata))
    self.assertGreater(len(run_metadata.step_stats.dev_stats), 0)
