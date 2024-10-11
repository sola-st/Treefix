# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with session.Session(server.target, config=self._useRPCConfig()) as sess:
    feed_val = np.empty([10000, 3000], dtype=np.float32)
    feed_val.fill(0.5)
    p = array_ops.placeholder(dtypes.float32, shape=[10000, 3000])
    min_t = math_ops.reduce_min(p)
    max_t = math_ops.reduce_max(p)
    min_val, max_val = sess.run([min_t, max_t], feed_dict={p: feed_val})
    self.assertEqual(0.5, min_val)
    self.assertEqual(0.5, max_val)
