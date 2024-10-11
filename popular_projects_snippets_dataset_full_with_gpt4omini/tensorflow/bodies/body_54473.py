# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default() as g:
    sleep_op = test_ops.sleep_op(10)
    with self.session(graph=g) as sess:
        run_options = config_pb2.RunOptions(timeout_in_ms=3_000)
        with self.assertRaises(errors.DeadlineExceededError):
            sess.run(sleep_op, options=run_options)
