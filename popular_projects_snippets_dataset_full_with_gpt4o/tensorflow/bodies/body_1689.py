# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
with self.session():
    for dtype in self.numeric_tf_types:
        params = array_ops.placeholder(dtype=dtype)
        indices = array_ops.placeholder(dtype=np.int32)
        with self.test_scope():
            gather = array_ops.gather(params, indices)
        self.assertAllEqual(
            7, gather.eval(feed_dict={params: [4, 7, 2], indices: 1}))
        self.assertAllEqual(
            [7], gather.eval(feed_dict={params: [4, 7, 2], indices: [1]}))
        self.assertAllEqual(
            [[7]], gather.eval(feed_dict={params: [4, 7, 2], indices: [[1]]}))
