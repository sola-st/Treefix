# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    ph = array_ops.placeholder(dtypes.float32)
    a = math_ops.add(ph, 1.0)
    callable_opts = config_pb2.CallableOptions()
    callable_opts.feed.append(ph.name)
    callable_opts.fetch.append(a.name)
    for _ in range(3):
        callable_fn = sess._make_callable_from_options(callable_opts)
        for _ in range(5):
            self.assertEqual([2.0], callable_fn(np.array(1.0, dtype=np.float32)))
