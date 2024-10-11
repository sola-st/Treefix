# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.SOFTWARE_TRACE)
run_metadata = config_pb2.RunMetadata()

with ops.device('/cpu:0'):
    with session.Session() as sess:
        # all combinations are valid
        sess.run(constant_op.constant(1.0), options=None, run_metadata=None)
        sess.run(
            constant_op.constant(1.0), options=None, run_metadata=run_metadata)
        self.assertFalse(run_metadata.HasField('step_stats'))

        sess.run(
            constant_op.constant(1.0), options=run_options, run_metadata=None)
        self.assertFalse(run_metadata.HasField('step_stats'))

        sess.run(
            constant_op.constant(1.0),
            options=run_options,
            run_metadata=run_metadata)

        self.assertTrue(run_metadata.HasField('step_stats'))
        self.assertEqual(len(run_metadata.step_stats.dev_stats), 1)
