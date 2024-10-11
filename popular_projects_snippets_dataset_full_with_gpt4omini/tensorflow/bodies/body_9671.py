# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = variables.Variable(42.0)
    b = state_ops.assign_add(a, 1.0)
    sess.run(a.initializer)
    tensor_runner = sess.make_callable(b.op, accept_options=True)
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()
    self.assertEqual(0, len(run_metadata.step_stats.dev_stats))
    tensor_runner(options=run_options, run_metadata=run_metadata)
    self.assertEqual(43.0, sess.run(a))
    self.assertGreater(len(run_metadata.step_stats.dev_stats), 0)
