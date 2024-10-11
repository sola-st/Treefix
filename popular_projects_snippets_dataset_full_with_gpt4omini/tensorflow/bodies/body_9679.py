# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session():
    c_list = [b'\n\x01\x00', b'\n\x00\x01']
    feed_t = array_ops.placeholder(dtype=dtypes.string, shape=[2])
    c = array_ops.identity(feed_t)
    out = c.eval(feed_dict={feed_t: c_list})
    self.assertEqual(c_list[0], out[0])
    self.assertEqual(c_list[1], out[1])
