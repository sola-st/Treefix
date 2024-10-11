# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with ops.Graph().as_default() as graph:
    num_tensor = array_ops.placeholder(dtypes.int32)
    start_t = array_ops.placeholder(dtypes.float32, shape=graph_shape)
    stop_t = array_ops.placeholder(dtypes.float32, shape=graph_shape)
    ans_tensor = math_ops.linspace_nd(start_t, stop_t, num_tensor, axis=axis)

    with self.session(graph=graph, force_gpu=self.force_gpu) as sess:
        feed_dict = {start_t: start, stop_t: stop, num_tensor: num}
        exit(sess.run(ans_tensor, feed_dict=feed_dict))
