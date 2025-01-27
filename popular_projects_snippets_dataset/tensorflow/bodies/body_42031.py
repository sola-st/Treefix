# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/graph_only_ops_test.py
with ops.Graph().as_default():
    x_tf = graph_only_ops.graph_placeholder(dtypes.int32, shape=(1,))
    y_tf = math_ops.square(x_tf)
    with self.cached_session() as sess:
        x = np.array([42])
        y = sess.run(y_tf, feed_dict={x_tf: np.array([42])})
        self.assertAllClose(np.square(x), y)
