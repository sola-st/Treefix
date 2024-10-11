# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default() as g:
    get_deadline = test_ops.get_deadline()
    with self.session(graph=g) as sess:
        run_options = config_pb2.RunOptions()
        with self.assertRaises(errors.InvalidArgumentError):
            sess.run(get_deadline, options=run_options)
