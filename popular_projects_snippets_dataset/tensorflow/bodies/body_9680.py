# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session():
    c_list = [
        u'\n\x01\x00', u'\n\x00\x01', u'\u26a3 unicode',
        u'\U0001f60e deal with it'
    ]
    feed_t = array_ops.placeholder(dtype=dtypes.string, shape=[len(c_list)])
    c = array_ops.identity(feed_t)

    out = c.eval(feed_dict={feed_t: c_list})
    for i in range(len(c_list)):
        self.assertEqual(c_list[i], out[i].decode('utf-8'))

    out = c.eval(feed_dict={feed_t: np.array(c_list, dtype=np.object_)})
    for i in range(len(c_list)):
        self.assertEqual(c_list[i], out[i].decode('utf-8'))
