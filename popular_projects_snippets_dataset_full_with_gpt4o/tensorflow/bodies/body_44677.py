# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with self.cached_session() as sess:
    p = array_ops.placeholder(dtype=dtypes.int32, shape=None)
    t = py_builtins.len_(p)
    self.assertEqual(sess.run(t, {p: [1, 2, 3]}), 3)

    with self.assertRaises(errors_impl.InvalidArgumentError):
        t = py_builtins.len_(p)
        sess.run(t, {p: 1})
