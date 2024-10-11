# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py

class SquaredTensor(object):

    def __init__(self, tensor):
        self.sq = math_ops.square(tensor)

fetch_fn = lambda squared_tensor: ([squared_tensor.sq], lambda val: val[0])
feed_fn1 = lambda feed, feed_val: [(feed.sq, feed_val)]
feed_fn2 = lambda feed: [feed.sq]

session.register_session_run_conversion_functions(SquaredTensor, fetch_fn,
                                                  feed_fn1, feed_fn2)
with self.assertRaises(ValueError):
    session.register_session_run_conversion_functions(SquaredTensor, fetch_fn,
                                                      feed_fn1, feed_fn2)
with self.cached_session() as sess:
    np1 = np.array([1.0, 1.5, 2.0, 2.5])
    np2 = np.array([3.0, 3.5, 4.0, 4.5])
    squared_tensor = SquaredTensor(np2)
    squared_eval = sess.run(squared_tensor)
    self.assertAllClose(np2 * np2, squared_eval)
    squared_eval = sess.run(
        squared_tensor, feed_dict={
            squared_tensor: np1 * np1
        })
    self.assertAllClose(np1 * np1, squared_eval)
    partial_run = sess.partial_run_setup([squared_tensor], [])
    squared_eval = sess.partial_run(partial_run, squared_tensor)
    self.assertAllClose(np2 * np2, squared_eval)
