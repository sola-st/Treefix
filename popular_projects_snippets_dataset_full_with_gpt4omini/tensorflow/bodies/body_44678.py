# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
try:
    out_capturer = io.StringIO()
    sys.stdout = out_capturer
    with self.cached_session() as sess:
        sess.run(py_builtins.print_(constant_op.constant('test message'), 1))
        self.assertEqual(out_capturer.getvalue(), 'test message 1\n')
finally:
    sys.stdout = sys.__stdout__
