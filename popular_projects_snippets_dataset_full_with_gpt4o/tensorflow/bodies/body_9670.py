# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(42.0)
    tensor_runner = sess.make_callable(a, accept_options=True)
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()
    self.assertEqual(0, len(run_metadata.step_stats.dev_stats))
    res = tensor_runner(options=run_options, run_metadata=run_metadata)
    self.assertEqual(42.0, res)
    self.assertGreater(len(run_metadata.step_stats.dev_stats), 0)
